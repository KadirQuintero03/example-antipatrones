from app.repositories.csv_repository import CSVRepository
from app.repositories.json_repository import JSONRepository

async def process_csv_usecase(file, csv_repo=None, json_repo=None):
    csv_repo = csv_repo or CSVRepository()
    json_repo = json_repo or JSONRepository()
    data = csv_repo.read_csv(file)
    json_repo.save_json(data)
    return "Procesado y guardado como JSON."
