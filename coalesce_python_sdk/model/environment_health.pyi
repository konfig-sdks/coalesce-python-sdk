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


class EnvironmentHealth(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def DELETING(cls):
        return cls("Deleting")
    
    @schemas.classproperty
    def DEPLOYING(cls):
        return cls("Deploying")
    
    @schemas.classproperty
    def FAILED_DEPLOY(cls):
        return cls("Failed Deploy")
    
    @schemas.classproperty
    def FAILED_DEV_RUN(cls):
        return cls("Failed Dev Run")
    
    @schemas.classproperty
    def FAILED_REFRESH(cls):
        return cls("Failed Refresh")
    
    @schemas.classproperty
    def INITIALIZING(cls):
        return cls("Initializing")
    
    @schemas.classproperty
    def REFRESHING(cls):
        return cls("Refreshing")
    
    @schemas.classproperty
    def RUNNING_DEV_RUN(cls):
        return cls("Running Dev Run")
    
    @schemas.classproperty
    def WAITING(cls):
        return cls("Waiting")
