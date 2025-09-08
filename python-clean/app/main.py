from fastapi import FastAPI, UploadFile, File
from app.usecases.process_csv_usecase import process_csv_usecase
from app.usecases.get_historical_usecase import get_historical_usecase
from app.repositories.csv_repository import CSVRepository
from app.repositories.json_repository import JSONRepository

app = FastAPI()

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    result = await process_csv_usecase(file, csv_repo=CSVRepository(), json_repo=JSONRepository())
    return {"message": result}

@app.get("/historical")
def get_historical():
    return get_historical_usecase(json_repo=JSONRepository())

## esta es la raiz app.use()