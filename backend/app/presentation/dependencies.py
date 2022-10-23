from service.service_prediction import ServicePrediction
from service.service_storage import ServiceStorage

_service_storage = ServiceStorage()
_service_prediction = ServicePrediction()


def get_service_prediction() -> ServicePrediction:
    return _service_prediction


def get_service_storage() -> ServiceStorage:
    return _service_storage
