from typing import Dict

class HttpRequest:
    """
        Class to represent the HTTP request
    """
    def __init__(
        self,
        header: Dict = None,
        body: Dict = None,
        quey_params: Dict = None,
    ) -> None:
        self.header = header
        self.body = body
        self.quey_params = quey_params
        