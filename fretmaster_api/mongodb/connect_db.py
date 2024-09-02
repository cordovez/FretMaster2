import motor.motor_asyncio


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("localhost", 27017)
    return client["fretmaster"]
