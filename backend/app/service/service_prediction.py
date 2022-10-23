import json
from datetime import date, datetime, timedelta
from random import randint
from typing import List, Optional

from core.settings import app_settings
from schemas.series import Series, SeriesData, SeriesResponse

float_precision = 3


class ServicePrediction:
    def __init__(self):
        self.precompiled_data = {
            "keeping": json.load(open("files/МСК 107_keeping_actual.json")),
            "receiving": json.load(open("files/СЗ_keeping_actual.json")),
            "shipment": json.load(open("files/Урал_keeping_actual.json")),
        }

    def _get_precompiled_data(self, from_: date, to_: date, precision_days: int):
        series = []
        for series_name, series_file in self.precompiled_data.items():
            series_data = []
            for key, value in series_file.items():
                date_compiled = datetime.strptime(key, "%Y-%m-%d").date()
                if from_ < date_compiled < to_:
                    series_data.append(
                        SeriesData(
                            x=date_compiled.replace(year=2022),
                            y=value + app_settings.data_offset,
                        )
                    )
            series.append(
                Series(
                    id=series_name,
                    data=sorted(
                        self._crop_data(series_data, precision_days),
                        key=lambda x: x.x,
                    ),
                )
            )
        return SeriesResponse(series=series)

    def get_data(
        self,
        delta: int,
        from_: Optional[date] = None,
        to_: Optional[date] = None,
        precision_days: int = 1,
    ) -> SeriesResponse:
        if from_ is None or to_ is None:
            from_ = date.today() - timedelta(days=delta) // 2
            to_ = date.today() + timedelta(days=delta) // 2
        return self._get_precompiled_data(from_, to_, precision_days)

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
    ) -> SeriesResponse:
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
