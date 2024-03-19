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


class Error(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "errorString",
        }
        
        class properties:
            errorString = schemas.StrSchema
            errorDetail = schemas.StrSchema
            __annotations__ = {
                "errorString": errorString,
                "errorDetail": errorDetail,
            }
    
    errorString: MetaOapg.properties.errorString
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorString"]) -> MetaOapg.properties.errorString: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorDetail"]) -> MetaOapg.properties.errorDetail: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errorString", "errorDetail", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorString"]) -> MetaOapg.properties.errorString: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorDetail"]) -> typing.Union[MetaOapg.properties.errorDetail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errorString", "errorDetail", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        errorString: typing.Union[MetaOapg.properties.errorString, str, ],
        errorDetail: typing.Union[MetaOapg.properties.errorDetail, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Error':
        return super().__new__(
            cls,
            *args,
            errorString=errorString,
            errorDetail=errorDetail,
            _configuration=_configuration,
            **kwargs,
        )
