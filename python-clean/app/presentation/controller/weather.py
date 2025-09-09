from fastapi import UploadFile

from app.domain.dtos.weather_data import WeatherUploadDTO
from app.usecases.process_weather import ProcessWeatherDataUseCase

class WeatherController:
    def __init__(self,service:ProcessWeatherDataUseCase) -> None:
        self._sevice = service
        pass
    
    async def upload_weather_data(self,file:UploadFile):
        upload_instancie = WeatherUploadDTO(
            filename= file.filename, # pyright: ignore[reportArgumentType]
            content= await file.read()
        )
        
        await self._sevice.execute(upload_instancie)
        
        return {"message": "Se ha guardado correctamente"}