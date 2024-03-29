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


class JobsTriggerRerunRequestUserCredentials(BaseModel):
    # Snowflake Account Username. Required when snowflakeAuthType is Basic
    snowflake_username: typing.Optional[str] = Field(None, alias='snowflakeUsername')

    # Snowflake Account password. Required when snowflakeAuthType is Basic
    snowflake_password: typing.Optional[str] = Field(None, alias='snowflakePassword')

    # The PEM-encoded private key to use when authenticating to Snowflake. Required when using the KeyPair authentication type. Newlines must be encoded as \"\\n\" within the request.
    snowflake_key_pair_key: typing.Optional[str] = Field(None, alias='snowflakeKeyPairKey')

    # The password to use to decrypt the private key. This is only applicable when the authentication type is KeyPair and the private key is encrypted.
    snowflake_key_pair_pass: typing.Optional[str] = Field(None, alias='snowflakeKeyPairPass')

    # Snowflake compute warehouse
    snowflake_warehouse: typing.Optional[str] = Field(None, alias='snowflakeWarehouse')

    # Snowflake user role
    snowflake_role: typing.Optional[str] = Field(None, alias='snowflakeRole')

    # Options: Basic | KeyPair | OAuth
    snowflake_auth_type: typing.Optional[str] = Field(None, alias='snowflakeAuthType')
    class Config:
        arbitrary_types_allowed = True
