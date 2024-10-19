import functools
from typing import Any, Callable, List, TypeVar, cast

from fastapi import HTTPException
from fastapi import status as http_status

from app.admin.models.admin import Admin
from app.admin.schemas.admin_role_type import AdminRoleType
from app.core.constant_variables import ADMIN_ACCESS_DENIED

Function = TypeVar("Function", bound=Callable[..., Any])


def check_admin_accessibility(
    role_types: List[AdminRoleType],
) -> Callable[[Function], Function]:
    def decorator(function: Function) -> Function:
        @functools.wraps(function)
        async def wrapped(*args, **kwargs):  # type: ignore
            admin: Admin = kwargs["admin"]
            if admin.role_type == AdminRoleType.SUPER_ADMIN:
                return await function(*args, **kwargs)
            if admin.role_type not in role_types:
                raise HTTPException(
                    status_code=http_status.HTTP_406_NOT_ACCEPTABLE,
                    detail=ADMIN_ACCESS_DENIED,
                )
            return await function(*args, **kwargs)

        return cast(Function, wrapped)

    return decorator
