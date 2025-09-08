import pandas as pd
import numpy as np
from typing import Dict, Any, List, Sequence
from datetime import datetime

class CSVRepository:
    def read_csv(self, file) -> pd.DataFrame:
        """Lee un archivo CSV y realiza las conversiones de tipos necesarias"""
        df = pd.read_csv(file.file)
        
        # Convertir tipos de datos
        if 'fecha' in df.columns:
            df['fecha'] = pd.to_datetime(df['fecha'])
        if 'temperatura' in df.columns:
            df['temperatura'] = pd.to_numeric(df['temperatura'], errors='coerce')
        if 'humedad' in df.columns:
            df['humedad'] = pd.to_numeric(df['humedad'], errors='coerce')
        
        return df

    def get_statistics(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Calcula estadísticas usando operaciones vectorizadas de pandas"""
        if df.empty:
            return {"error": "No hay datos para analizar"}

        fecha_min = df['fecha'].min()
        fecha_max = df['fecha'].max()

        stats = {
            "resumen_general": {
                "total_registros": int(len(df)),
                "ciudades_unicas": int(df['ciudad'].nunique()),
                "rango_fechas": {
                    "inicio": fecha_min.isoformat() if isinstance(fecha_min, datetime) else str(fecha_min),
                    "fin": fecha_max.isoformat() if isinstance(fecha_max, datetime) else str(fecha_max)
                }
            },
            "temperatura": {
                "promedio": float(df['temperatura'].mean()),
                "minima": float(df['temperatura'].min()),
                "maxima": float(df['temperatura'].max()),
                "desviacion_estandar": float(df['temperatura'].std())
            },
            "por_ciudad": self._get_city_stats(df)
        }

        if 'humedad' in df.columns:
            stats["humedad"] = {
                "promedio": float(df['humedad'].mean()),
                "minima": float(df['humedad'].min()),
                "maxima": float(df['humedad'].max())
            }

        return stats

    def _get_city_stats(self, df: pd.DataFrame) -> Dict[str, Dict[str, float]]:
        """Calcula estadísticas por ciudad"""
        city_stats: Dict[str, Dict[str, float]] = {}
        for city in df['ciudad'].unique():
            city_data = df[df['ciudad'] == city]
            city_stats[str(city)] = {
                "temperatura_promedio": float(city_data['temperatura'].mean()),
                "temperatura_max": float(city_data['temperatura'].max()),
                "temperatura_min": float(city_data['temperatura'].min()),
                "total_registros": float(len(city_data))
            }
        return city_stats

    def to_dict(self, df: pd.DataFrame) -> Sequence[Dict[str, Any]]:
        """Convierte el DataFrame a una secuencia de diccionarios"""
        return [
            {str(k): v for k, v in record.items()}
            for record in df.to_dict(orient="records")
        ]
