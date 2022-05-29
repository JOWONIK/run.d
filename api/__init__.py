from fastapi import APIRouter
from api.events import router as event_router

router = APIRouter()


router.include_router(event_router)