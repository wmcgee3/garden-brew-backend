from datetime import datetime, timezone
from typing import Optional

from fastapi import FastAPI

from app.schemas import LinkModel, MoonResponse, RootResponse

app = FastAPI(title="Garden Brew API", description="", version="0.0.0")


@app.get("/", response_model=RootResponse)
def root():
    return RootResponse(
        _links=[
            LinkModel(rel="self", href="/", method="GET"),
            LinkModel(rel="moon", href="/moon", method="GET"),
            LinkModel(rel="Swagger", href="/docs", method="GET"),
            LinkModel(rel="Redoc", href="/redoc", method="GET"),
            LinkModel(rel="OpenAPI", href="/openapi.json", method="GET"),
        ],
    )


@app.get("/moon", response_model=MoonResponse)
def moon(datetime_utc: Optional[datetime] = None):
    known_new_moon = datetime(2022, 3, 2, 17, 34, tzinfo=timezone.utc)
    if datetime_utc is None:
        datetime_utc = datetime.now(timezone.utc)
    days = (datetime_utc - known_new_moon).days % 29.53059
    return MoonResponse(
        _links=[
            LinkModel(rel="self", href="/moon", method="GET"),
        ],
        days=days,
    )
