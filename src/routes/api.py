from fastapi import APIRouter
from src.routes.urlconversion import urlconversion
from src.routes.soccer import registration
from src.routes.twoFA import twoFA
from src.routes.nlphub import nlphub


router = APIRouter()
# router.include_router(urlconversion.router)
# router.include_router(registration.router)
# router.include_router(twoFA.router)
router.include_router(nlphub.router)
