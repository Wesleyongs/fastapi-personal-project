from fastapi import APIRouter
from src.routes.urlconversion import urlconversion
from src.routes.soccer import registration
from src.routes.twoFA import twoFA
from src.routes.nlphub import nlphub


router = APIRouter()
# router.include_router(urlconversion.router)
# router.include_router(registration.router)
<<<<<<< HEAD
router.include_router(twoFA.router)
# router.include_router(nlphub.router)
=======
# router.include_router(twoFA.router)
router.include_router(nlphub.router)
>>>>>>> d8c7427bcb11a41c2dfc16da990692e86c4024bd
