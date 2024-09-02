async def insert(document: dict, db) -> dict:
    result = await db.test.insert_one(document)
    return {'success': str(result.inserted_id)}