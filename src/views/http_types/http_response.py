from typing import Dict

class HttpResponse:
    def __init__(self, status_code: int, headers: Dict, body: Dict) -> None:
        self.status_code = status_code
        self.headers = headers
        self.body = body
