from fastapi import FastAPI

fastapp = FastAPI()


@fastapp.get("/")
async def root():
    return {"message": "Welcome to RESTQL!"}
