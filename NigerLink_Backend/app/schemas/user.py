from app.schemas.base import SchemaModel

class UserCreate(SchemaModel):
    nom: str
    prenom: str
    email: str
    proffession: str
    nationnalite: str
    sexe: str
    phone: str
    deviceId: str
    deviceName: str
    password: str
    pays: str
    ville: str
    quartier: str
    
class UserInfo(SchemaModel):
    userId: int
    nom: str
    prenom: str
    email: str
    proffession: str
    nationnalite: str
    sexe: str
    phone: str
    photo: str | None
    deviceId: str | None
    deviceName: str | None
    role: str
    pays: str | None
    ville: str | None
    quartier: str | None
    
    
    

class UserLogin(SchemaModel):
    userLogin: str
    userPassword: str
    


class TokenResponse(SchemaModel):
    access_token: str
    token_type: str
    
class ResponseRestorePassword(SchemaModel):
    message: str
    userId: int
    passewordTemporaire: str