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


class RunsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A collection of runs.
    """


    class MetaOapg:
        required = {
            "data",
            "limit",
            "orderBy",
            "orderByDirection",
        }
        
        class properties:
            limit = schemas.IntSchema
        
            @staticmethod
            def orderByDirection() -> typing.Type['OrderByDirection']:
                return OrderByDirection
        
            @staticmethod
            def orderBy() -> typing.Type['RunsOrderBy']:
                return RunsOrderBy
            
            
            class data(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_0(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['RunSummary']:
                                return RunSummary
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['RunSummary'], typing.List['RunSummary']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'any_of_0':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'RunSummary':
                            return super().__getitem__(i)
                    
                    
                    class any_of_1(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['RunInfo']:
                                return RunInfo
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['RunInfo'], typing.List['RunInfo']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'any_of_1':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'RunInfo':
                            return super().__getitem__(i)
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'data':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "limit": limit,
                "orderByDirection": orderByDirection,
                "orderBy": orderBy,
                "data": data,
            }
    
    data: MetaOapg.properties.data
    limit: MetaOapg.properties.limit
    orderBy: 'RunsOrderBy'
    orderByDirection: 'OrderByDirection'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderByDirection"]) -> 'OrderByDirection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderBy"]) -> 'RunsOrderBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["limit", "orderByDirection", "orderBy", "data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderByDirection"]) -> 'OrderByDirection': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderBy"]) -> 'RunsOrderBy': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["limit", "orderByDirection", "orderBy", "data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        limit: typing.Union[MetaOapg.properties.limit, decimal.Decimal, int, ],
        orderBy: 'RunsOrderBy',
        orderByDirection: 'OrderByDirection',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RunsResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            limit=limit,
            orderBy=orderBy,
            orderByDirection=orderByDirection,
            _configuration=_configuration,
            **kwargs,
        )

from coalesce_python_sdk.model.order_by_direction import OrderByDirection
from coalesce_python_sdk.model.run_info import RunInfo
from coalesce_python_sdk.model.run_summary import RunSummary
from coalesce_python_sdk.model.runs_order_by import RunsOrderBy