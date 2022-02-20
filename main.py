from fastapi import FastAPI
from app.routes import users,relationship,group


app = FastAPI()

app.include_router(users)
app.include_router(relationship)
app.include_router(group)


