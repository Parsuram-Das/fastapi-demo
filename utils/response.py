def success_response(message:str,data:None):
    return {"status": "success", "message": message, "data": data}
def error_response(message:str,status_code:int):
    return {"status": "error", "message": message, "data": None},status_code