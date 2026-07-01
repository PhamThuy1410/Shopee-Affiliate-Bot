from fastapi import FastAPI

app = FastAPI(title="Shopee Affiliate Bot")


@app.get("/")
def root():
    return {
        "message": "Shopee Affiliate Bot is running"
    }