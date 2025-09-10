from fastapi import APIRouter,UploadFile,File

from app.usecases.process_weather import ProcessWeatherDataUseCase
from app.presentation.controller.weather import WeatherController
from app.insfractuctura.factories.parser_factory import factory_parser
from app.repositories.weather_repository import RepositoryWeather

router = APIRouter(prefix='/weather',tags=['files'])

def moduleRouter():
    
    repository = RepositoryWeather()
    factory_parser_ = factory_parser()
    service = ProcessWeatherDataUseCase(factory_parser_,repository)
    controller = WeatherController(service)    
    
    @router.post('/')
    async def upload_csv(file:UploadFile = File(...)):
        return await controller.upload_weather_data(file=file)
        
    @router.get('/')
    def get_historical():
        return controller.get_weather()
    
    return router