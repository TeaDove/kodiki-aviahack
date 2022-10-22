from service.service_prediction import ServicePrediction

service_prediction = ServicePrediction()


class TestClass:
    async def test_get_mock_ok(self):
        result = service_prediction.get_mocked_data(delta=10, precision_days=4)
        print(result.series)

        assert len(result.series) == 3
        for series in result.series:
            assert len(series.data) == 2
