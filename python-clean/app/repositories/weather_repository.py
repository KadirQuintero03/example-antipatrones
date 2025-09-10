from app.domain.entities.WeatherDataCollection import WeatherDataCollection

cache_weather_list = []

class RepositoryWeather:
    def save(self,weather_list:WeatherDataCollection):
        cache_weather_list.extend(weather_list.get_data())
    
    def get_weather(self):
        return cache_weather_list