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

from coalesce_python_sdk.type.jobs_initiate_run400_response_error import JobsInitiateRun400ResponseError

class RequiredJobsInitiateRun400Response(TypedDict):
    pass

class OptionalJobsInitiateRun400Response(TypedDict, total=False):
    error: JobsInitiateRun400ResponseError

class JobsInitiateRun400Response(RequiredJobsInitiateRun400Response, OptionalJobsInitiateRun400Response):
    pass
