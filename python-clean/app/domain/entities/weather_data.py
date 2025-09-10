from dataclasses import dataclass
import datetime


@dataclass
class WeatherData:
    timestamp: str
    city: str
    unity: str
    temperature: float
    
    # Getters
    def get_timestamp(self) -> str:
        return self.timestamp
    
    def get_city(self) -> str:
        return self.city
    
    def get_unity(self) -> str:
        return self.unity
    
    def get_temperature(self) -> float:
        return self.temperature
    
    # Setters
    def set_timestamp(self, timestamp: str) -> None:
        self.timestamp = timestamp
    
    def set_city(self, city: str) -> None:
        self.city = city
    
    def set_unity(self, unity: str) -> None:
        self.unity = unity
    
    def set_temperature(self, temperature: float) -> None:
        if not isinstance(temperature, (int, float)):
            raise ValueError("Temperature must be a number")
        self.temperature = float(temperature)
    
    # Método para convertir a diccionario
    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "city": self.city,
            "unity": self.unity,
            "temperature": self.temperature
        }
    