from pydantic import BaseModel


class Symbol(BaseModel):
    symbol: str


class Symbols(BaseModel):
    symbols: list[Symbol]
