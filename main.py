from fastapi import FastAPI
import models
from database import engine
from routers import user, authentication, fakultas, prodi, biodata

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)

app.include_router(fakultas.router)
app.include_router(prodi.router)
app.include_router(biodata.router)
