from dataclasses import asdict, dataclass
from typing import Generic, Optional, Type, TypeVar

from neomodel import StructuredNode, adb

ModelType = TypeVar("ModelType", bound=StructuredNode)
CreateSchemaType = TypeVar("CreateSchemaType", bound=dataclass)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=dataclass)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_by_uid(
        self,
        obj_uid: str,
    ) -> Optional[ModelType]:
        obj = self.model.nodes.get_or_none(uid=obj_uid)
        return obj

    async def create(
        self,
        create_schema: CreateSchemaType,
    ) -> ModelType:
        res = self.model(**asdict(create_schema)).save()
        return res

    async def get_or_create(
        self,
        create_schema: CreateSchemaType,
    ) -> ModelType:
        res = self.model(**asdict(create_schema)).get_or_create()
        return res

    async def remove(self, obj_uid: str) -> bool:
        obj = await self.get_by_uid(obj_uid=obj_uid)
        if obj:
            obj.delete()
            return True
        return False

    async def update(
        self,
        obj_uid: str,
        update_schema: UpdateSchemaType,
    ) -> Optional[ModelType]:
        obj = await self.get_by_uid(obj_uid=obj_uid)
        if obj:
            for field, value in asdict(update_schema).items():
                if value is not None:
                    setattr(obj, field, value)
            return obj.save()
        return None

    async def remove_all_relationships(self, instance: ModelType) -> None:
        cypher_query = """
        MATCH (n)-[r]-() WHERE elementId(n) = '$elementID'
        DELETE r
        """
        cypher_query = cypher_query.replace("$elementID", instance.element_id)
        await adb.cypher_query(cypher_query)
