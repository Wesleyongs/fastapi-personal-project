import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# local
from src.routes.api import router as api_router

app = FastAPI(openapi_url='/openapi.json',  # This line solved my issue, in my case it was a lambda function
              root_path="/ dev")
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


@app.get("/test")
async def test():
    return {"message": "This proves that FastAPI routes is not working in deployment mode"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
