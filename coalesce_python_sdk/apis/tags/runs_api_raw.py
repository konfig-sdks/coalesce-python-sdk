# coding: utf-8

"""
    Coalesce API

    REST API for performing operations with the Coalesce backend.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from coalesce_python_sdk.paths.api_v1_runs_run_id.get import GetRunDetailsRaw
from coalesce_python_sdk.paths.api_v1_runs.get import ListInformationRaw
from coalesce_python_sdk.paths.api_v1_runs_run_id_results.get import ListResultsRaw


class RunsApiRaw(
    GetRunDetailsRaw,
    ListInformationRaw,
    ListResultsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass