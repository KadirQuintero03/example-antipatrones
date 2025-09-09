from fastapi import APIRouter,UploadFile,File

from app.usecases.process_weather import ProcessWeatherDataUseCase
from app.presentation.controller.weather import WeatherController
from app.insfractuctura.factories.parser_factory import factory_parser

router = APIRouter(prefix='/file',tags=['files'])

def moduleRouter():
    
    factory_parser_ = factory_parser()
    service = ProcessWeatherDataUseCase(factory_parser_)
    controller = WeatherController(service)    
    
    router.post('/')
    async def upload_csv(file:UploadFile = File(...)):
        return await controller.upload_weather_data(file=file)
        
    
    router.get('/historical')
    def get_historical():
        return
    
    return router