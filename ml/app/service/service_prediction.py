from datetime import date, timedelta
from random import randint
from typing import List, Optional

from schemas.series import SeriesData, SeriesResponse

float_precision = 3


class ServicePrediction:
    def _get_random_data(
        self, delta: int, from_: Optional[date] = None, to_: Optional[date] = None
    ) -> List[SeriesData]:
        if not (from_ is None or to_ is None):
            return [
                SeriesData(x=from_ + timedelta(days=i), y=randint(1, 10))
                for i in range((to_ - from_).days)
            ]
        else:
            return [
                SeriesData(
                    x=date.today() + timedelta(days=(i - delta // 2)),
                    y=randint(1, 10),
                )
                for i in range(delta)
            ]

    def _crop_data(
        self, series: List[SeriesData], precision_days: int
    ) -> List[SeriesData]:
        to_return = []
        for i in range(len(series) // precision_days):
            batch = series[i * precision_days : (i + 1) * precision_days]
            avg_value = round(
                sum((v.y for v in batch)) / precision_days, float_precision
            )
            to_return.append(SeriesData(x=batch[0].x, y=avg_value))
        return to_return

    def get_mocked_data(
        self,
        delta: int = 30,
        from_: Optional[date] = None,
        to_: Optional[date] = None,
        precision_days: int = 1,
    ):
        if precision_days == 1:
            return SeriesResponse.parse_obj(
                {
                    "series": [
                        {
                            "id": "keeping",
                            "data": self._get_random_data(delta, from_, to_),
                        },
                        {
                            "id": "receiving",
                            "data": self._get_random_data(delta, from_, to_),
                        },
                        {
                            "id": "shipment",
                            "data": self._get_random_data(delta, from_, to_),
                        },
                    ]
                }
            )

        return SeriesResponse.parse_obj(
            {
                "series": [
                    {
                        "id": "keeping",
                        "data": self._crop_data(
                            self._get_random_data(delta, from_, to_), precision_days
                        ),
                    },
                    {
                        "id": "receiving",
                        "data": self._crop_data(
                            self._get_random_data(delta, from_, to_), precision_days
                        ),
                    },
                    {
                        "id": "shipment",
                        "data": self._crop_data(
                            self._get_random_data(delta, from_, to_), precision_days
                        ),
                    },
                ]
            }
        )
