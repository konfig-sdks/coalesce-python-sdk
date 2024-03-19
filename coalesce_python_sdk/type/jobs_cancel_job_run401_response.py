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

from coalesce_python_sdk.type.jobs_cancel_job_run401_response_error import JobsCancelJobRun401ResponseError

class RequiredJobsCancelJobRun401Response(TypedDict):
    pass

class OptionalJobsCancelJobRun401Response(TypedDict, total=False):
    error: JobsCancelJobRun401ResponseError

class JobsCancelJobRun401Response(RequiredJobsCancelJobRun401Response, OptionalJobsCancelJobRun401Response):
    pass