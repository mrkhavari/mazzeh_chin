from passlib.context import CryptContext


async def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return bool(
        CryptContext(schemes=["bcrypt"], deprecated="auto").verify(
            plain_password,
            hashed_password,
        ),
    )
