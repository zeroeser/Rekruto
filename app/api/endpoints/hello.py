from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def say_hello(name: str,
                    message: str):
    return f"Hello {name}! {message}"
