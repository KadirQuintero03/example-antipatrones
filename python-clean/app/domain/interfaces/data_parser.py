from abc import ABC,abstractmethod
from app.domain.entities.WeatherDataCollection import WeatherDataCollection

class DataParser(ABC):
    @abstractmethod
    def parse(self,path:str) -> WeatherDataCollection:
        pass