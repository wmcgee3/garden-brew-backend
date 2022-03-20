from typing import List, Literal

from pydantic import BaseModel, Field, constr


class LinkModel(BaseModel):
    rel: str
    href: constr(regex="^/.*$")  # must start with `/`
    method: Literal[
        "GET",
        "HEAD",
        "POST",
        "PUT",
        "DELETE",
        "CONNECT",
        "OPTIONS",
        "TRACE",
        "PATCH",
    ]


class BaseResponse(BaseModel):
    links: List[LinkModel] = Field(..., alias="_links")


class RootResponse(BaseResponse):
    pass


class MoonResponse(BaseResponse):
    days: int
