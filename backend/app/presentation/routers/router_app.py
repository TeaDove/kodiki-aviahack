from datetime import date, timedelta
from random import randint
from typing import Any, Dict, List

from fastapi import APIRouter, Depends

from presentation.auth_utils import get_yc_token
from presentation.dependencies import get_service_app
from presentation.logs_utils import LoggerRouteHandler
from schemas.series import SeriesResponse
from service.service_app import ServiceApp

router = APIRouter(prefix="", route_class=LoggerRouteHandler)


@router.get("/")
async def hello_world(
    service_app: ServiceApp = Depends(get_service_app), _: str = Depends(get_yc_token)
) -> str:
    return await service_app.process_request()


def get_random_data(size: int) -> List[Dict[str, Any]]:
    return [
        {"x": date.today() + timedelta(days=i), "y": randint(1, 10)}
        for i in range(size)
    ]


@router.get("/series-mock", response_model=SeriesResponse)
def get_series_mock(size: int = 30) -> SeriesResponse:
    return SeriesResponse.parse_obj(
        {
            "series": [
                {"id": "keeping", "data": get_random_data(size)},
                {"id": "receiving", "data": get_random_data(size)},
                {"id": "shipment", "data": get_random_data(size)},
            ]
        }
    )
