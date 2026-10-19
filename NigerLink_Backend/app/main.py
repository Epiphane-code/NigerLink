from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.user import router as user_router, routerPublic as user_routerPublic
from app.routers.chaine import router as chaine_router, routerPublic as chaine_routerPublic, routerPrivate2 as chaine_routerPrivate2
from app.routers.palace import router as palace_router, routerPublic as palace_routerPublic, routerPrivate2 as palace_private2
from app.routers.diffusion import router as diff_router, routerPublic as diff_routerPublic
from app.routers.commentaire import router as commentaire_router, routerPublic as commentairePublic_router


app = FastAPI(title= "Api NigerLink")

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(user_routerPublic)
app.include_router(palace_router)
app.include_router(palace_routerPublic)
app.include_router(palace_private2)
app.include_router(chaine_router)
app.include_router(chaine_routerPublic)
app.include_router(chaine_routerPrivate2)
app.include_router(diff_router)
app.include_router(diff_routerPublic)
app.include_router(commentaire_router)
app.include_router(commentairePublic_router)