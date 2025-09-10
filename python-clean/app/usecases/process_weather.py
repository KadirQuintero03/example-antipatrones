from app.insfractuctura.factories.parser_factory import factory_parser
from app.repositories.weather_repository import RepositoryWeather
from app.domain.dtos.weather_data import WeatherUploadDTO
import tempfile
import os

class ProcessWeatherDataUseCase:
    def __init__(self, parser_factory: factory_parser, repository:RepositoryWeather):
        self._parser_factory = parser_factory
        self._repository = repository
    
    async def execute(self, upload_dto: WeatherUploadDTO):
        upload_dto.validate()
    
        temp_path = await self._save_temp_file(upload_dto)
        try:
            parser = self._parser_factory.create_parser(upload_dto.file_extension)
            
            weather_data = parser.parse(path=temp_path)
            
            self._repository.save(weather_data)
        finally:
            # 6. Limpiar archivo temporal
            os.remove(temp_path)
            
    async def _save_temp_file(self,file:WeatherUploadDTO):
        
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file.content)
            temp_file_path = temp_file.name
        return temp_file_path
    
    
    def get_weather_all(self):
        return self._repository.get_weather()