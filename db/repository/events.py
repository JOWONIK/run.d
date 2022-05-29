import db


async def get_events():
    return await db.MongoDataBase.db['us_member'].find({}, {'_id': 0}).to_list(length=100)


async def insert_one_event(event_in_model):
    result = await db.MongoDataBase.db['event'].insert_one(event_in_model.dict())
    return result.inserted_id
