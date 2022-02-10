import logging.config

import yaml
from fastapi import FastAPI

from app.api.router import api_router
from app.config import settings

app = FastAPI(title="SERVICE_NAME")


def configure_logging():
    with open(settings.LOGGING_CONF_PATH) as f:
        logging_conf = yaml.load(f, Loader=yaml.FullLoader)
    logging.config.dictConfig(logging_conf)


@app.on_event("startup")
async def startup():
    configure_logging()


app.include_router(api_router)
