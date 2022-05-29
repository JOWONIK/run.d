import motor.motor_asyncio
import logging
from bson import ObjectId


class MongoDataBase(object):
    client = None
    db = None

    def __new__(cls):
        logging.info("Connection mongo db......")
        if not hasattr(cls,'instance'):
            cls.instance = super(MongoDataBase, cls).__new__(cls)
            conn_str = "mongodb+srv://wonya:1q2w3e4r5t6y7u8i9o0p@simpool.qolzp.mongodb.net/?retryWrites=true&w=majority"
            cls.client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
            cls.db = cls.client['simpool']

            logging.info("Connected mongo db")
        else:
            logging.error("몽고 디비 싱글톤 깨짐쓰~")
        return cls.instance


class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')