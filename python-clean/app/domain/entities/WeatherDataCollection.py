from typing import List
from app.domain.entities.weather_data import WeatherData

class WeatherDataCollection:
    def __init__(self, data_list: List[WeatherData]):
        self._data = data_list
    
    def get_data(self) -> List[WeatherData]:
        return self._data