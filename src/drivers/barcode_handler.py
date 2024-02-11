from barcode import Code128
from barcode.writer import ImageWriter

class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        path__from_tag = f'{tag}'
        tag.save(path__from_tag)

        return path__from_tag
