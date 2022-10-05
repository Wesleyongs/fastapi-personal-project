from fastapi import APIRouter
from src.routes.urlconversion import urlconversion
from src.routes.soccer import registration


router = APIRouter()
router.include_router(urlconversion.router)
router.include_router(registration.router)
