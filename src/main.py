import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# local
from src.routes.api import router as api_router

app = FastAPI()

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
