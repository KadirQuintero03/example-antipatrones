from dataclasses import dataclass
import datetime


@dataclass
class WeatherData:
    timestamp: str
    city: str
    unity: str
    temperature: float