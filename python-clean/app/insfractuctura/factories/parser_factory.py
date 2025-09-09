from app.insfractuctura.parsers.csv_parser import CSVWeatherParser
from app.insfractuctura.parsers.json_parser import JSONWeatherParser
from app.insfractuctura.parsers.xml_parser import XMLWeatherParser
from app.domain.interfaces.data_parser import DataParser

class factory_parser:
    def __init__(self) -> None:
        self._parser = {
            '.xml': XMLWeatherParser,
            '.json':JSONWeatherParser,
            '.csv':CSVWeatherParser
        }
        pass
    
    def create_parser(self,file_extension:str) -> DataParser:
        parser_class = self._parser.get(file_extension.lower())
        if not parser_class:
            raise ValueError(f"Unsupported file format: {file_extension}")
        return parser_class