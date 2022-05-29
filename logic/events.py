import db.repository.events as event_repo


async def get_events():
    return await event_repo.get_events()


async def insert_one_events(event_in_model):
    return await event_repo.insert_one_event(event_in_model)