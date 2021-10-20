from fastapi import FastAPI
from .exceptions import init_exceptions
from .middlewares import init_middlewares

from .featurename.v1.api import router

app = FastAPI(
    title="Your Project Title In Documentation",
    decription="Your Project Description",
    version="0.0.1" #Your Project Version
)

init_exceptions(app)
init_middlewares(app)

# init your app router
app.include_router(router, prefix="/v1") # go to localhost:8000/v1