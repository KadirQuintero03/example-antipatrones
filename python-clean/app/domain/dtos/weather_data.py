# domain/dtos/weather_upload_dto.py
from dataclasses import dataclass
from pathlib import Path


@dataclass
class WeatherUploadDTO:
    filename: str
    content: bytes
    
    @property
    def file_extension(self) -> str:
        return Path(self.filename).suffix.lower()
    
    def validate(self) -> bool:
        if not self.filename:
            raise ValueError("Filename is required")
        
        if self.file_extension not in ['.csv', '.json', '.xml']:
            raise ValueError(f"Unsupported file format: {self.file_extension}")
        
        return True