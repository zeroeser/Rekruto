from typing import Awaitable, Callable, Union

from fastapi import APIRouter, FastAPI
from fastapi.openapi.models import Response

from app.settings import Settings
from app.dto.health_state import HealthState


def init_fast_api(
    settings: Settings,
    router: APIRouter,
    health_check_callback: Callable[
        [Response], Union[HealthState, Awaitable[HealthState]]
    ],
) -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME)

    # Добавление роута для проверки статуса сервиса
    router.add_api_route(
        "/health",
        health_check_callback,
        response_model=HealthState,
        methods=["get"],
        summary="Get service status",
        tags=["Maintenance"],
    )

    app.include_router(router, prefix=settings.API_PATH)

    return app
