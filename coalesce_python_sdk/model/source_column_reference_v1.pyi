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


class SourceColumnReferenceV1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "transform",
            "columnReferences",
        }
        
        class properties:
            
            
            class columnReferences(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ColumnReference']:
                        return ColumnReference
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ColumnReference'], typing.List['ColumnReference']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'columnReferences':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ColumnReference':
                    return super().__getitem__(i)
            transform = schemas.StrSchema
            __annotations__ = {
                "columnReferences": columnReferences,
                "transform": transform,
            }
    
    transform: MetaOapg.properties.transform
    columnReferences: MetaOapg.properties.columnReferences
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columnReferences"]) -> MetaOapg.properties.columnReferences: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transform"]) -> MetaOapg.properties.transform: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["columnReferences", "transform", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columnReferences"]) -> MetaOapg.properties.columnReferences: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transform"]) -> MetaOapg.properties.transform: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["columnReferences", "transform", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        transform: typing.Union[MetaOapg.properties.transform, str, ],
        columnReferences: typing.Union[MetaOapg.properties.columnReferences, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SourceColumnReferenceV1':
        return super().__new__(
            cls,
            *args,
            transform=transform,
            columnReferences=columnReferences,
            _configuration=_configuration,
            **kwargs,
        )

from coalesce_python_sdk.model.column_reference import ColumnReference