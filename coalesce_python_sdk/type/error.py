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


class RequiredError(TypedDict):
    # The error message.
    errorString: str

class OptionalError(TypedDict, total=False):
    # Additional detail about the error.
    errorDetail: str

class Error(RequiredError, OptionalError):
    pass
