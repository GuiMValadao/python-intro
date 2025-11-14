from fastapi import FastAPI

from controllers import item

app = FastAPI()
app.include_router(item.router)
