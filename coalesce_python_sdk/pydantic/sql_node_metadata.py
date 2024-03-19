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

from coalesce_python_sdk.pydantic.column_metadata import ColumnMetadata
from coalesce_python_sdk.pydantic.node_test import NodeTest
from coalesce_python_sdk.pydantic.source_map import SourceMap
from coalesce_python_sdk.pydantic.sql_node_metadata_enabled_column_test_ids import SQLNodeMetadataEnabledColumnTestIDs
from coalesce_python_sdk.pydantic.sql_node_metadata_mapping import SQLNodeMetadataMapping

class SQLNodeMetadata(BaseModel):
    applied_node_tests: typing.List[NodeTest] = Field(alias='appliedNodeTests')

    columns: typing.List[ColumnMetadata] = Field(alias='columns')

    enabled_column_test_i_ds: SQLNodeMetadataEnabledColumnTestIDs = Field(alias='enabledColumnTestIDs')

    source_mapping: typing.List[SourceMap] = Field(alias='sourceMapping')

    description: typing.Optional[str] = Field(None, alias='description')

    cte_string: typing.Optional[str] = Field(None, alias='cteString')

    destination_name: typing.Optional[str] = Field(None, alias='destinationName')

    mapping: typing.Optional[SQLNodeMetadataMapping] = Field(None, alias='mapping')

    materialization_option: typing.Optional[str] = Field(None, alias='materializationOption')
    class Config:
        arbitrary_types_allowed = True
