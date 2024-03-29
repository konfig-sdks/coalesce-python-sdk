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

from coalesce_python_sdk.pydantic.jobs_trigger_rerun_request_run_details import JobsTriggerRerunRequestRunDetails
from coalesce_python_sdk.pydantic.jobs_trigger_rerun_request_user_credentials import JobsTriggerRerunRequestUserCredentials

class JobsTriggerRerunRequest(BaseModel):
    run_details: JobsTriggerRerunRequestRunDetails = Field(alias='runDetails')

    user_credentials: JobsTriggerRerunRequestUserCredentials = Field(alias='userCredentials')

    # Contains parameters to be used in the Refresh
    parameters: typing.Optional[str] = Field(None, alias='parameters')
    class Config:
        arbitrary_types_allowed = True
