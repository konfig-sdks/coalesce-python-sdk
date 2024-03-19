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

from coalesce_python_sdk.type.user_connection_type import UserConnectionType

class RequiredSnowflakeUserCredentials(TypedDict):
    snowflakeAccount: str

    snowflakeAuthType: UserConnectionType

    snowflakeUsername: str

class OptionalSnowflakeUserCredentials(TypedDict, total=False):
    snowflakeRole: str

    snowflakeWarehouse: str

class SnowflakeUserCredentials(RequiredSnowflakeUserCredentials, OptionalSnowflakeUserCredentials):
    pass
