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

from coalesce_python_sdk.pydantic.registry_package_result_public_releases import RegistryPackageResultPublicReleases
from coalesce_python_sdk.pydantic.registry_package_result_updated_at import RegistryPackageResultUpdatedAt

class RegistryPackageResult(BaseModel):
    description: str = Field(alias='description')

    name: str = Field(alias='name')

    org: str = Field(alias='org')

    latest_release: str = Field(alias='latestRelease')

    id: str = Field(alias='id')

    public_releases: RegistryPackageResultPublicReleases = Field(alias='publicReleases')

    updated_by: typing.Optional[str] = Field(None, alias='updatedBy')

    updated_at: typing.Optional[RegistryPackageResultUpdatedAt] = Field(None, alias='updatedAt')
    class Config:
        arbitrary_types_allowed = True
