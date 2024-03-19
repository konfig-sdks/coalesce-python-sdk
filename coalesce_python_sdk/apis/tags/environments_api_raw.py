# coding: utf-8

"""
    Coalesce API

    REST API for performing operations with the Coalesce backend.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from coalesce_python_sdk.paths.api_v1_environments_environment_id.get import GetInformationRaw
from coalesce_python_sdk.paths.api_v1_environments.get import ListInformationRaw


class EnvironmentsApiRaw(
    GetInformationRaw,
    ListInformationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
