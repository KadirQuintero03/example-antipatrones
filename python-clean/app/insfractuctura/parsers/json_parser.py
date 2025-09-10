from app.domain.interfaces.data_parser import DataParser
from app.domain.entities.WeatherDataCollection import WeatherDataCollection

class JSONWeatherParser(DataParser):
    def __init__(self) -> None:
        pass
    
    def parse(self,path:str) -> WeatherDataCollection:
        weather_list = []
        return WeatherDataCollection(weather_list)
    