from fastapi import APIRouter
from app.pkg.redis_tools.tools import RedisTools


router = APIRouter(prefix="/api/v1/currency")


@router.get("/{pair}")
async def get_currency_pair(pair: str):
    price = await RedisTools.get_pair(pair)
    if not price:
        return {"error": "This pair doesn't exists"}

    return {"pair": pair, "price": price}
