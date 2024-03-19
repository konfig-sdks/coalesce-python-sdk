# coding: utf-8

"""
    Coalesce API

    REST API for performing operations with the Coalesce backend.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from coalesce_python_sdk.paths.api_v1_environments_environment_id_nodes_node_id.get import GetInformation
from coalesce_python_sdk.paths.api_v1_environments_environment_id_nodes.get import List
from coalesce_python_sdk.apis.tags.nodes_api_raw import NodesApiRaw


class NodesApi(
    GetInformation,
    List,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: NodesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = NodesApiRaw(api_client)
