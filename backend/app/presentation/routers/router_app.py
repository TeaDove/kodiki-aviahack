from random import randint

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


@router.get("/series-mock", response_model=SeriesResponse)
def get_series_mock() -> SeriesResponse:
    return SeriesResponse.parse_obj(
        {
            "series": [
                {
                    "id": "keeping",
                    "data": [
                        {"x": randint(1, 10), "y": randint(1, 10)}
                        for _ in range(randint(10, 20))
                    ],
                },
                {
                    "id": "receiving",
                    "data": [
                        {"x": randint(1, 10), "y": randint(1, 10)}
                        for _ in range(randint(10, 20))
                    ],
                },
                {
                    "id": "shipment",
                    "data": [
                        {"x": randint(1, 10), "y": randint(1, 10)}
                        for _ in range(randint(10, 20))
                    ],
                },
            ]
        }
    )
