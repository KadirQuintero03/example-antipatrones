from typing import Optional, Dict, Any
from app.repositories.csv_repository import CSVRepository
from app.repositories.json_repository import JSONRepository

async def process_csv_usecase(
    file,
    csv_repository: Optional[CSVRepository] = None,
    json_repository: Optional[JSONRepository] = None
) -> Dict[str, Any]:
    """
    Procesa un archivo CSV con datos meteorológicos usando pandas
    para un procesamiento eficiente y análisis estadístico
    """
    # Inyección de dependencias
    csv_repository = csv_repository or CSVRepository()
    json_repository = json_repository or JSONRepository()
    
    # Lectura y procesamiento del CSV usando pandas
    df = csv_repository.read_csv(file)
    
    # Calcular estadísticas
    statistics = csv_repository.get_statistics(df)
    
    # Preparar datos para guardar
    processed_data = {
        "data": csv_repository.to_dict(df),
        "statistics": statistics,
        "metadata": {
            "filename": file.filename if hasattr(file, 'filename') else "unknown",
            "total_records": len(df),
            "columns": list(df.columns)
        }
    }
    
    # Guardar resultados
    json_repository.save_json(processed_data)
    
    return {
        "message": "Datos procesados exitosamente con análisis estadístico",
        "summary": {
            "total_records": len(df),
            "cities": df['ciudad'].unique().tolist(),
            "date_range": {
                "start": df['fecha'].min().isoformat(),
                "end": df['fecha'].max().isoformat()
            }
        }
    }
