import pandas as pd

class CSVRepository:
    def read_csv(self, file):
        df = pd.read_csv(file.file)
        return df.to_dict(orient="records")
