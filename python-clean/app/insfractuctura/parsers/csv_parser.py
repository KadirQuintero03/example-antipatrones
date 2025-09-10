from app.domain.interfaces.data_parser import DataParser
from app.domain.entities.WeatherDataCollection import WeatherDataCollection
from app.domain.entities.weather_data import WeatherData

import pandas as pd

class CSVWeatherParser(DataParser):
    
    def parse(self,path:str) -> WeatherDataCollection:
        df = pd.read_csv(path)
        weather_list = []
        for _,row in df.iterrows():
            print(row)
            weather_data = WeatherData(
                timestamp=row['fecha'],
                city=str(row['ciudad']).strip(),
                temperature=float(row['temperatura']),
                unity=str(row['unidad']).strip()
            )
            weather_list.append(weather_data)
        
        return WeatherDataCollection(weather_list)
    
    
    