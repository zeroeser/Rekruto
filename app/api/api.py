from fastapi import APIRouter

from .endpoints import hello

api_router = APIRouter()


api_router.include_router(
    hello.router,
    prefix="",
    tags=["Тест"],
)
