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

from coalesce_python_sdk.type.base_environment import BaseEnvironment
from coalesce_python_sdk.type.environment_summary import EnvironmentSummary

class RequiredEnvironmentsResponse(TypedDict):
    # A collection of environment information.
    data: typing.Union[typing.List[EnvironmentSummary], typing.List[BaseEnvironment]]

class OptionalEnvironmentsResponse(TypedDict, total=False):
    pass

class EnvironmentsResponse(RequiredEnvironmentsResponse, OptionalEnvironmentsResponse):
    pass