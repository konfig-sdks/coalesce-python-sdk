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

from coalesce_python_sdk.pydantic.query_result import QueryResult

class RunResult(BaseModel):
    is_running: bool = Field(alias='isRunning')

    name: str = Field(alias='name')

    node_i_d: str = Field(alias='nodeID')

    query_results: typing.List[QueryResult] = Field(alias='queryResults')

    render_query_result: typing.Optional[QueryResult] = Field(None, alias='renderQueryResult')
    class Config:
        arbitrary_types_allowed = True
