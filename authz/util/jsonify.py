from flask import current_app

DEBUG_MSG_CODES = {
    "100": "OK",
    "101": "Unsupported Media Type",
    "102": "Database Error",
    "103": "Resource Not Found",
    "104": "Request Validation Failed",
    "105": "Empty Data Supplied",
    "106": "Resource Confilct",
    "107": "Not Impleamented",
    "108": "Resource Expired",
    "109": "Bad Desired Status",
    "110": "Token Encryption Error",
    "111": "Resouce Not Match",
    "112": "Header Not Specified",
    "113": "Token Validation Error",
    "114": "Invalid Token Data",
    "115": "Controll Allowed Roles Not Found",
    "116": "Resource Access Denied",
    "117": "Role Not Found"
}


def jsonify(state={}, metadata={}, status=200, code=100, headers={}):
    data = state
    data.update(metadata)
    if current_app.debug:
        data["message"] = DEBUG_MSG_CODES[str(code)]
    data["code"] = code
    return data, state, headers
