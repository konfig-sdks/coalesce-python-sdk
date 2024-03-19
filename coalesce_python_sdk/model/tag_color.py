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


class TagColor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            backgroundColor = schemas.StrSchema
            textColor = schemas.StrSchema
            __annotations__ = {
                "backgroundColor": backgroundColor,
                "textColor": textColor,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backgroundColor"]) -> MetaOapg.properties.backgroundColor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["textColor"]) -> MetaOapg.properties.textColor: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["backgroundColor", "textColor", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backgroundColor"]) -> typing.Union[MetaOapg.properties.backgroundColor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["textColor"]) -> typing.Union[MetaOapg.properties.textColor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["backgroundColor", "textColor", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        backgroundColor: typing.Union[MetaOapg.properties.backgroundColor, str, schemas.Unset] = schemas.unset,
        textColor: typing.Union[MetaOapg.properties.textColor, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TagColor':
        return super().__new__(
            cls,
            *args,
            backgroundColor=backgroundColor,
            textColor=textColor,
            _configuration=_configuration,
            **kwargs,
        )
