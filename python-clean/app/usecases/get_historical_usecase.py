from app.repositories.json_repository import JSONRepository

def get_historical_usecase(json_repo=None):
    json_repo = json_repo or JSONRepository()
    return json_repo.load_json()