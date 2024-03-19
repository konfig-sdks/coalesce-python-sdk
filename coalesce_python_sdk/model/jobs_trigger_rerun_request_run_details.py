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


class JobsTriggerRerunRequestRunDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Contains the runID to be re-run.
    """


    class MetaOapg:
        required = {
            "runID",
        }
        
        class properties:
            runID = schemas.StrSchema
            forceIgnoreWorkspaceStatus = schemas.BoolSchema
            __annotations__ = {
                "runID": runID,
                "forceIgnoreWorkspaceStatus": forceIgnoreWorkspaceStatus,
            }
    
    runID: MetaOapg.properties.runID
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runID"]) -> MetaOapg.properties.runID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forceIgnoreWorkspaceStatus"]) -> MetaOapg.properties.forceIgnoreWorkspaceStatus: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["runID", "forceIgnoreWorkspaceStatus", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runID"]) -> MetaOapg.properties.runID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forceIgnoreWorkspaceStatus"]) -> typing.Union[MetaOapg.properties.forceIgnoreWorkspaceStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["runID", "forceIgnoreWorkspaceStatus", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        runID: typing.Union[MetaOapg.properties.runID, str, ],
        forceIgnoreWorkspaceStatus: typing.Union[MetaOapg.properties.forceIgnoreWorkspaceStatus, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobsTriggerRerunRequestRunDetails':
        return super().__new__(
            cls,
            *args,
            runID=runID,
            forceIgnoreWorkspaceStatus=forceIgnoreWorkspaceStatus,
            _configuration=_configuration,
            **kwargs,
        )