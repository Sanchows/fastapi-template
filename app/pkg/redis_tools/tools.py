import redis.asyncio

from app.configuration import config


class RedisTools:
    __redis_connect = redis.asyncio.Redis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        decode_responses=True,
    )

    @classmethod
    async def set_pair(cls, pair: str, price: str):
        await cls.__redis_connect.set(pair, price)

    @classmethod
    async def get_pair(cls, pair):
        return await cls.__redis_connect.get(pair)

    @classmethod
    async def get_keys(cls):
        return await cls.__redis_connect.keys(pattern="*")
