import traceback

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse

from . import api
from .version import VERSION


app = FastAPI(version=VERSION, title='Gamal', description="Welcome to Gamal, the API for camels!")


@app.exception_handler(Exception)
def generic_error_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": str(exc), "traceback": traceback.format_tb(exc.__traceback__)})


@app.get("/", include_in_schema=False)
async def root():
    return HTMLResponse(api.random_camel_html(), 200)


@app.get("/random_camel_base64")
async def random_camel_base64():
    return api.random_camel_base64()
