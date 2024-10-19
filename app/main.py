from fastapi import FastAPI


def get_application() -> FastAPI:
    application = FastAPI()
    return application


app: FastAPI = get_application()
