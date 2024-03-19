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


class ColumnReference(BaseModel):
    column_i_d: str = Field(alias='columnID')

    node_i_d: str = Field(alias='nodeID')
    class Config:
        arbitrary_types_allowed = True