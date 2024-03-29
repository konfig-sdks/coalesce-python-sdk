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


class RequiredJobsInitiateRun401ResponseError(TypedDict):
    pass

class OptionalJobsInitiateRun401ResponseError(TypedDict, total=False):
    errorString: str

    errorDetail: str

class JobsInitiateRun401ResponseError(RequiredJobsInitiateRun401ResponseError, OptionalJobsInitiateRun401ResponseError):
    pass
