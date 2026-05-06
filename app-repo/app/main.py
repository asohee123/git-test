from fastapi import FastAPI
from app.core.config import settings
from app.routers import items

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(items.router)


@app.get("/health")
def health():
    return {"status": "ok", "version": settings.APP_VERSION}
