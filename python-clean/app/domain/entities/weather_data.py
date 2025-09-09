from dataclasses import dataclass
import datetime


@dataclass
class WeatherData:
    temperature: float
    humidity: float
    timestamp: datetime.datetime
    station_id: str