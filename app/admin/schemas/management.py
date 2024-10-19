from dataclasses import dataclass

from app.admin.schemas.admin_role_type import AdminRoleType

@dataclass
class CreateAdminInputSchema:
    username: str
    password: str
    role_type: AdminRoleType
    

@dataclass
class CreateAdminOutputSchema:
    uid: str
    username: str
    role_type: AdminRoleType
    time_created: str
    

@dataclass
class AdminSchema:
    username: str
    password: str
    role_type: str
    
    
@dataclass
class AdminOutputSchema:
    uid: str
    username: str
    role_type: AdminRoleType
    time_created: str