from datetime import date
from typing import List

from schemas.base import ConfigBaseModel


class SeriesData(ConfigBaseModel):
    x: date
    y: float


class Series(ConfigBaseModel):
    id: str
    data: List[SeriesData]


class SeriesResponse(ConfigBaseModel):
    series: List[Series]
