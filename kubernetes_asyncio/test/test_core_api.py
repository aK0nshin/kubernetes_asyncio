# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.core_api import CoreApi  # noqa: E501
from kubernetes.client.rest import ApiException


class TestCoreApi(unittest.TestCase):
    """CoreApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.core_api.CoreApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_versions(self):
        """Test case for get_api_versions

        """
        pass


if __name__ == '__main__':
    unittest.main()