# coding: utf-8

"""
    Coalesce API

    REST API for performing operations with the Coalesce backend.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class Error(BaseModel):
    # The error message.
    error_string: str = Field(alias='errorString')

    # Additional detail about the error.
    error_detail: typing.Optional[str] = Field(None, alias='errorDetail')
    class Config:
        arbitrary_types_allowed = True
