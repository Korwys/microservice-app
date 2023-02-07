from starlette.responses import JSONResponse


def error_notification() -> JSONResponse:
    return JSONResponse(status_code=400, content={"Message": "Something went wrong. Please try again later"})
