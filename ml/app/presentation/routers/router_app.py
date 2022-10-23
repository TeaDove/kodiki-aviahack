from fastapi import APIRouter, Depends, UploadFile

from presentation.dependencies import get_service_prediction
from presentation.logs_utils import LoggerRouteHandler
from service.service_prediction import ServicePrediction

router = APIRouter(prefix="", route_class=LoggerRouteHandler)


@router.post("/predict")
def upload_weights(
    file: UploadFile,
    service_prediction: ServicePrediction = Depends(get_service_prediction),
):
    ...
