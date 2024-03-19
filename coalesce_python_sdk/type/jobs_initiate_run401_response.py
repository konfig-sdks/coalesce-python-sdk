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

from coalesce_python_sdk.type.jobs_initiate_run401_response_error import JobsInitiateRun401ResponseError

class RequiredJobsInitiateRun401Response(TypedDict):
    pass

class OptionalJobsInitiateRun401Response(TypedDict, total=False):
    error: JobsInitiateRun401ResponseError

class JobsInitiateRun401Response(RequiredJobsInitiateRun401Response, OptionalJobsInitiateRun401Response):
    pass
