from fastapi import APIRouter
from logic import events as event_logic
from api.model.event_model import InsertEventInModel


router = APIRouter(
    prefix="/event",
    tags=["event"]
)


@router.get("")
async def get_events():
    return await event_logic.get_events()


@router.post("")
async def insert_event(model: InsertEventInModel):
    print(model)
    id = await event_logic.insert_one_events(model)
    print(id)
