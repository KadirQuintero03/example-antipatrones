from app.insfractuctura.factories.parser_factory import factory_parser
from app.domain.dtos.weather_data import WeatherUploadDTO

import os

class ProcessWeatherDataUseCase:
    def __init__(self, parser_factory: factory_parser):
        self._parser_factory = parser_factory
    
    async def execute(self, upload_dto: WeatherUploadDTO):
        # 1. Validar DTO
        upload_dto.validate()
        
        # 2. Guardar archivo temporalmente
        temp_path = await self._save_temp_file(upload_dto)
        
        try:
            # 3. Obtener parser apropiado
            parser = self._parser_factory.create_parser(upload_dto.file_extension)
            
            # 4. Parsear datos
            weather_data = parser.parse(temp_path)
            
            
        finally:
            # 6. Limpiar archivo temporal
            os.remove(temp_path)
            
    async def _save_temp_file(self,file:WeatherUploadDTO):
        temp_file_path = f"/temp/{file.filename}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(file.content)
        return temp_file_path