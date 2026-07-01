from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Shopee Affiliate Bot",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Shopee Affiliate Bot is running"
    }