from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, Query, UploadFile

from presentation.dependencies import get_service_prediction, get_service_storage
from presentation.logs_utils import LoggerRouteHandler
from schemas.series import SeriesResponse
from service.service_prediction import ServicePrediction
from service.service_storage import ServiceStorage

router = APIRouter(prefix="", route_class=LoggerRouteHandler)


@router.get("/series", response_model=SeriesResponse)
def get_series(
    service_prediction: ServicePrediction = Depends(get_service_prediction),
) -> SeriesResponse:
    return service_prediction.get_data()


@router.get("/series-mock", response_model=SeriesResponse)
def get_series_mock(
    delta: int = 30,
    from_: Optional[date] = Query(None, alias="from"),
    to_: Optional[date] = Query(None, alias="to"),
    service_prediction: ServicePrediction = Depends(get_service_prediction),
    precision_days: int = Query(3, alias="precisionDays"),
) -> SeriesResponse:
    return service_prediction.get_mocked_data(delta, from_, to_, precision_days)


@router.post("/weights")
def upload_weights(
    file: UploadFile,
    service_storage: ServiceStorage = Depends(get_service_storage),
):
    return service_storage.safe_weights_file(file)
