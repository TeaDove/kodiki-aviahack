from fastapi import APIRouter, Depends, UploadFile

from presentation.dependencies import get_service_storage
from presentation.logs_utils import LoggerRouteHandler
from service.service_storage import ServiceStorage

router = APIRouter(prefix="", route_class=LoggerRouteHandler)


@router.post("/predict")
def upload_weights(
    file: UploadFile,
    service_storage: ServiceStorage = Depends(get_service_storage),
):
    return service_storage.safe_weights_file(file)
