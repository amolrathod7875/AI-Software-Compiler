from typing import Dict, Any, Optional, List
from pydantic import BaseModel, model_validator

class UIComponent(BaseModel):
    type: str
    name: str
    props: Dict[str, Any] = {}

class UIConfig(BaseModel):
    components: List[UIComponent] = []
    layout: str = "default"

class APIEndpoint(BaseModel):
    path: str
    method: str
    auth_required: bool = False
    request_body: Optional[Dict[str, Any]] = None
    response_schema: Optional[Dict[str, Any]] = None

class APIConfig(BaseModel):
    endpoints: List[APIEndpoint] = []
    auth_required: bool = False

class DBTable(BaseModel):
    name: str
    fields: List[Dict[str, str]] = []

class DBModel(BaseModel):
    name: str
    table: str
    fields: Dict[str, Any] = {}

class DBConfig(BaseModel):
    tables: List[DBTable] = []
    models: List[DBModel] = []

class AuthProvider(BaseModel):
    name: str
    type: str

class AuthRole(BaseModel):
    name: str
    permissions: List[str] = []

class AuthConfig(BaseModel):
    providers: List[AuthProvider] = []
    roles: List[AuthRole] = []

class AppConfig(BaseModel):
    ui: Optional[UIConfig] = None
    api: Optional[APIConfig] = None
    db: Optional[DBConfig] = None
    auth: Optional[AuthConfig] = None

    @model_validator(mode='after')
    def cross_layer_consistency(self):
        if self.auth and self.auth.providers and not self.api:
            self.api = APIConfig(auth_required=True)
        return self