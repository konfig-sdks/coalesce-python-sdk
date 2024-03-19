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

from coalesce_python_sdk.type.error import Error

class RequiredQueryResult(TypedDict):
    isRunning: bool

    name: str

    sql: str

    status: str

    success: bool

class OptionalQueryResult(TypedDict, total=False):
    endTime: datetime

    error: Error

    queryID: str

    rowsDeleted: int

    rowsInserted: int

    rowsUpdated: int

    startTime: datetime

    warehouse: str

class QueryResult(RequiredQueryResult, OptionalQueryResult):
    pass