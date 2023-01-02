import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# local
from src.routes.api import router as api_router

description = """
This app is automatically built and deployed whenever a push is made to the github main branch. It consist of the following features

## URL Shortener
All transactions are stored in a persistent SQL table

## 2FA
You will be able to:

* **Generate 2FA** (_Twillio SMS only works with registered mobile numbers_).
* **Authenticate** (_Generated 2FAs are valid for 60s_).
"""
app = FastAPI(title="Python Backend Microservices",
              description=description,
              version="0.0.1",
              contact={
                  "name": "Wesley Ong",
                  "url": "https://wesleyongs.com",
                  "email": "wesleyispro@gmail.com",
              },
              license_info={
                  "name": "GitHub Repo",
                  "url": "https://github.com/Wesleyongs/fastapi-personal-project", },)


app.include_router(api_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello! how are u, i am underwater"}


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
