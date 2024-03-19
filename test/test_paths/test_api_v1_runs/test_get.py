# coding: utf-8

"""
    Coalesce API

    REST API for performing operations with the Coalesce backend.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import coalesce_python_sdk
from coalesce_python_sdk.paths.api_v1_runs import get
from coalesce_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1Runs(ApiTestMixin, unittest.TestCase):
    """
    ApiV1Runs unit test stubs
        List Runs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
