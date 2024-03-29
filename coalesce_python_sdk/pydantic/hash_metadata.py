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

from coalesce_python_sdk.pydantic.column_reference import ColumnReference
from coalesce_python_sdk.pydantic.hash_algorithm import HashAlgorithm

class HashMetadata(BaseModel):
    hash_algorithm: HashAlgorithm = Field(alias='hashAlgorithm')

    hash_type: typing.Optional[Literal["ChangeHash", "Hash", "HubHash", "LinkHash", "None"]] = Field(None, alias='hashType')

    hub_hashes: typing.Optional[typing.List[ColumnReference]] = Field(None, alias='hubHashes')
    class Config:
        arbitrary_types_allowed = True
