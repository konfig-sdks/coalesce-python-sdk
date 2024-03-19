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


class IntermediateColumnRefResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "columnName",
            "tableName",
        }
        
        class properties:
            columnName = schemas.StrSchema
            
            
            class tableName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tableName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "columnName": columnName,
                "tableName": tableName,
            }
    
    columnName: MetaOapg.properties.columnName
    tableName: MetaOapg.properties.tableName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columnName"]) -> MetaOapg.properties.columnName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tableName"]) -> MetaOapg.properties.tableName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["columnName", "tableName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columnName"]) -> MetaOapg.properties.columnName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tableName"]) -> MetaOapg.properties.tableName: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["columnName", "tableName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        columnName: typing.Union[MetaOapg.properties.columnName, str, ],
        tableName: typing.Union[MetaOapg.properties.tableName, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IntermediateColumnRefResult':
        return super().__new__(
            cls,
            *args,
            columnName=columnName,
            tableName=tableName,
            _configuration=_configuration,
            **kwargs,
        )
