from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class TagCreatorController:
    '''
        Responsability for implementing business rules
    '''

    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_tag(product_code)
        formatted_response = self.__formate_response(path_from_tag)
        return formatted_response
    
    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        return barcode_handler.create_barcode(product_code)
    
    def __formate_response(self, path_from_tag: str) -> Dict:
        return {'data': {
            "type": "Tag Image",
            "count": 1,
            "path": f'{path_from_tag}.png',
        }}