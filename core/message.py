# def base_response(code, msg, data=None):
#     if data is None:
#         data = []
#     result = {
#         "code": code,
#         "message": msg,
#         "data": data
#     }
#     return result

def the_response(code: bool, data: list, total: int):
    return {"code": code, "data": data, "total": total}

def success(msg=''):
    return {"code": 200, "message": msg }

def fail(msg=''):
    return {"code": -1, "message": msg }

def notfound(msg=''):
    return {"code": 404, "message": msg }

def invalid(msg=''):
    return {"code": 401, "message": msg }