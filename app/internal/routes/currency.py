from fastapi import APIRouter, Depends
from app.pkg.redis_tools.tools import RedisTools


router = APIRouter(prefix="/api/v1/currency")


@router.get("/{pair}")
async def get_currency_pair(
    pair: str, keys: list = Depends(RedisTools.get_keys)
):
    if pair not in [s for s in keys]:
        return {"error": "This pair doesn't exists"}

    return {"pair": pair, "price": await RedisTools.get_pair(pair)}
