from neo4j import AsyncDriver, AsyncGraphDatabase, AsyncSession

from app.core.config import get_settings

neo4j_driver: AsyncDriver = None


async def get_session() -> AsyncSession:
    global neo4j_driver
    if not neo4j_driver:
        neo4j_driver = AsyncGraphDatabase.driver(
            get_settings().NEO4J_BOLT_URL,
            auth=(get_settings().NEO4J_USERNAME, get_settings().NEO4J_PASSWORD),
        )
    async with neo4j_driver.session() as session:
        try:
            yield session
        finally:
            await session.close()
