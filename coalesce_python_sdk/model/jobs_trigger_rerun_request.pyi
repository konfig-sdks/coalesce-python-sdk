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


class JobsTriggerRerunRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "userCredentials",
            "runDetails",
        }
        
        class properties:
        
            @staticmethod
            def runDetails() -> typing.Type['JobsTriggerRerunRequestRunDetails']:
                return JobsTriggerRerunRequestRunDetails
        
            @staticmethod
            def userCredentials() -> typing.Type['JobsTriggerRerunRequestUserCredentials']:
                return JobsTriggerRerunRequestUserCredentials
            parameters = schemas.StrSchema
            __annotations__ = {
                "runDetails": runDetails,
                "userCredentials": userCredentials,
                "parameters": parameters,
            }
    
    userCredentials: 'JobsTriggerRerunRequestUserCredentials'
    runDetails: 'JobsTriggerRerunRequestRunDetails'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runDetails"]) -> 'JobsTriggerRerunRequestRunDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userCredentials"]) -> 'JobsTriggerRerunRequestUserCredentials': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parameters"]) -> MetaOapg.properties.parameters: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["runDetails", "userCredentials", "parameters", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runDetails"]) -> 'JobsTriggerRerunRequestRunDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userCredentials"]) -> 'JobsTriggerRerunRequestUserCredentials': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parameters"]) -> typing.Union[MetaOapg.properties.parameters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["runDetails", "userCredentials", "parameters", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        userCredentials: 'JobsTriggerRerunRequestUserCredentials',
        runDetails: 'JobsTriggerRerunRequestRunDetails',
        parameters: typing.Union[MetaOapg.properties.parameters, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobsTriggerRerunRequest':
        return super().__new__(
            cls,
            *args,
            userCredentials=userCredentials,
            runDetails=runDetails,
            parameters=parameters,
            _configuration=_configuration,
            **kwargs,
        )

from coalesce_python_sdk.model.jobs_trigger_rerun_request_run_details import JobsTriggerRerunRequestRunDetails
from coalesce_python_sdk.model.jobs_trigger_rerun_request_user_credentials import JobsTriggerRerunRequestUserCredentials
