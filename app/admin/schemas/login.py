from dataclasses import dataclass
from typing import Optional


@dataclass
class AdminLoginOutputSchema:
    access_token: str
    expires_in: str
    token_type: Optional[str] = "Bearer"
