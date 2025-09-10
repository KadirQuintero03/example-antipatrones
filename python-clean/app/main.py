from fastapi import FastAPI, UploadFile, File

from app.usecases.get_historical_usecase import get_historical_usecase
from app.repositories.csv_repository import CSVRepository
from app.repositories.json_repository import JSONRepository

from app.presentation.routes import routes 

app = FastAPI()

app.include_router(routes.moduleRouter(),prefix='/api')

@app.get('/')
def get_health():
    return {"message": "I Life"}

@app.get("/historical")
def get_historical():
    return get_historical_usecase(json_repo=JSONRepository())

## esta es la raiz app.use()
