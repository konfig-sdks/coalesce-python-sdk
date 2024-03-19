# coding: utf-8

"""
    Coalesce API

    REST API for performing operations with the Coalesce backend.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from coalesce_python_sdk import schemas  # noqa: F401


class BaseNode(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "schema",
            "database",
            "locationName",
            "name",
            "description",
            "id",
            "nodeType",
        }
        
        class properties:
            description = schemas.StrSchema
            database = schemas.StrSchema
            id = schemas.StrSchema
            locationName = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def nodeType() -> typing.Type['NodeType']:
                return NodeType
            schema = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "database": database,
                "id": id,
                "locationName": locationName,
                "name": name,
                "nodeType": nodeType,
                "schema": schema,
            }
        additional_properties = schemas.AnyTypeSchema
    
    schema: MetaOapg.properties.schema
    database: MetaOapg.properties.database
    locationName: MetaOapg.properties.locationName
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    nodeType: 'NodeType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema"]) -> MetaOapg.properties.schema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["database"]) -> MetaOapg.properties.database: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationName"]) -> MetaOapg.properties.locationName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeType"]) -> 'NodeType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["schema"], typing_extensions.Literal["database"], typing_extensions.Literal["locationName"], typing_extensions.Literal["name"], typing_extensions.Literal["description"], typing_extensions.Literal["id"], typing_extensions.Literal["nodeType"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema"]) -> MetaOapg.properties.schema: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["database"]) -> MetaOapg.properties.database: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationName"]) -> MetaOapg.properties.locationName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeType"]) -> 'NodeType': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["schema"], typing_extensions.Literal["database"], typing_extensions.Literal["locationName"], typing_extensions.Literal["name"], typing_extensions.Literal["description"], typing_extensions.Literal["id"], typing_extensions.Literal["nodeType"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        schema: typing.Union[MetaOapg.properties.schema, str, ],
        database: typing.Union[MetaOapg.properties.database, str, ],
        locationName: typing.Union[MetaOapg.properties.locationName, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        nodeType: 'NodeType',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'BaseNode':
        return super().__new__(
            cls,
            *args,
            schema=schema,
            database=database,
            locationName=locationName,
            name=name,
            description=description,
            id=id,
            nodeType=nodeType,
            _configuration=_configuration,
            **kwargs,
        )

from coalesce_python_sdk.model.node_type import NodeType
