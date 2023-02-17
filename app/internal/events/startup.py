import aiohttp

from app.configuration import config
from app.internal.schemas.currency import Symbols
from app.pkg.redis_tools.tools import RedisTools


async def on_startup():
    async with aiohttp.ClientSession() as session:
        async with session.get(config.ALL_PAIRS_URL) as response:
            response_json = await response.json()

            parsed_pairs = Symbols(**response_json)

            cutted_pairs = parsed_pairs.symbols[:20]

            symbols = [pair.symbol for pair in cutted_pairs]

            for symbol in symbols:
                await RedisTools.set_pair(symbol, 0)


async def on_loop_startup():
    for symbol in await RedisTools.get_keys():
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{config.CURRENCY_PAIR_URL}{symbol}"
            ) as response:
                response_json = await response.json()
                await RedisTools.set_pair(symbol, response_json["price"])
