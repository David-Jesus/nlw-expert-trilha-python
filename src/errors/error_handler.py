from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        # Enviar para um log ou Email
        return HttpResponse(
            status_code=error.status_code,
            headers={},
            body={
                'errors': [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    
    return HttpResponse(
        status_code=500,
        headers={},
        body={
            'errors': [{
                "title": "Sever Error",
                "detail": str(error)
            }]
        }
    )
