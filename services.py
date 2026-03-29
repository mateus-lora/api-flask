from database import DataRepository

class DataService:
    def __init__(self):
        self.repository = DataRepository()

    def process_new_data(self, value) -> None:
        if value is None or not str(value).strip():
            raise ValueError("O valor fornecido é nulo ou inválido.")
        
        self.repository.insert(str(value))

    def retrieve_formatted_data(self) -> list:
        rows = self.repository.get_all()
        return [{"id": row[0], "data": row[1]} for row in rows]