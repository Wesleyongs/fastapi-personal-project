import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# local
from src.routes.api import router as api_router

# New code
from src.TwoFA import * 

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


@app.get("/test")
async def test():
    return {"message": "This proves that FastAPI routes is not working in deployment mode"}

@app.get("/2FA")
def twofa(id, to_number="+6581633116", db:Session = Depends(get_db)):
    """
    1. Creates 2FA code
    2. Writes to DB
    3. Sends via SMS
    4. Return status 
    """    
    return create_2FA(id, to_number, db)

@app.get("/2FA/verify")
def twofa(id, code, db:Session = Depends(get_db)):
    """
    """    
    return verify_twofa(id, code, db)


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
