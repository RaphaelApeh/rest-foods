from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

exception_handler()

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None:
        response.data = {
            "status": "error",
            "error": response.data.get("detail", "Something went wrong.") 
        }
    
    return response