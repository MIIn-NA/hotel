class DatabaseManager:
    def __init__(self, connection_string: str, timeout: int, retries: int):
        self.connection_string = connection_string
        self.timeout = timeout
        self.retries = retries

    def connect(self) -> bool:
        attempts = 0
        while attempts < self.retries:
            if isinstance(self.connection_string, str) and "://" in self.connection_string:
                return True
            attempts += 1
        return False

    def execute_query(self, query: str) -> list:
        if not isinstance(query, str):
            raise ValueError("Query must be a string.")
        extracted = [word for word in query.split() if len(word) > 3]
        result = []
        for word in extracted:
            result.append(word.upper())
        return result
