from typing import Optional, Dict, Any, cast
import pandas as pd
from app.repositories.json_repository import JSONRepository

def get_historical_usecase(
    json_repo: Optional[JSONRepository] = None,
    filters: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Obtiene y filtra datos históricos usando pandas para
    un procesamiento eficiente
    """
    # Inyección de dependencias
    json_repo = json_repo or JSONRepository()
    
    # Cargar datos
    full_data = json_repo.load_json()
    
    # Asegurarnos de que full_data es un diccionario
    if not isinstance(full_data, dict):
        return {"error": "Formato de datos inválido", "data": []}
    
    # Si no hay filtros y los datos son válidos, retornar todos los datos
    if not filters:
        return cast(Dict[str, Any], full_data)
    
    # Validar que existan datos
    data_list = full_data.get("data", [])
    if not data_list:
        return {"error": "No hay datos disponibles", "data": []}
    
    # Convertir a DataFrame para filtrado eficiente
    df = pd.DataFrame(data_list)
    
    # Aplicar filtros si existen
    if df.empty:
        return {"data": [], "message": "No hay datos para filtrar"}
    
    if "ciudad" in filters and filters["ciudad"]:
        df = df[df["ciudad"] == filters["ciudad"]]
    
    if "fecha_inicio" in filters and filters["fecha_inicio"]:
        df = df[df["fecha"] >= filters["fecha_inicio"]]
    
    if "fecha_fin" in filters and filters["fecha_fin"]:
        df = df[df["fecha"] <= filters["fecha_fin"]]
    
    # Actualizar estadísticas para los datos filtrados
    filtered_data: Dict[str, Any] = {
        "data": [
            {str(k): v for k, v in record.items()}
            for record in df.to_dict(orient="records")
        ],
        "metadata": {
            "total_registros_originales": len(data_list),
            "total_registros_filtrados": len(df),
            "filtros_aplicados": filters
        }
    }
    
    return filtered_data
