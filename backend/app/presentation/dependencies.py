from service.service_prediction import ServicePrediction

_service_prediction = ServicePrediction()


def get_service_prediction():
    return _service_prediction
