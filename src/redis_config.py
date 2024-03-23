import aioredis
from aioredis import Redis


REDIS_URL = "redis://localhost"


redis: Redis = None


async def get_redis() -> Redis:
    global redis
    if redis is None:
        redis = await aioredis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
    return redis


async def close_redis():
    global redis
    if redis:
        await redis.close()
        redis = None
