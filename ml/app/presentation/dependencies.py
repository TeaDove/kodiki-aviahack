from service.service_prediction import ServicePrediction

_service_prediction = ServicePrediction()


def get_service_prediction() -> ServicePrediction:
    return _service_prediction
