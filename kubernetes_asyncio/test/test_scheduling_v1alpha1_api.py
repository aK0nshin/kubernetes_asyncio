# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.12.6
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.scheduling_v1alpha1_api import SchedulingV1alpha1Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestSchedulingV1alpha1Api(unittest.TestCase):
    """SchedulingV1alpha1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.scheduling_v1alpha1_api.SchedulingV1alpha1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_priority_class(self):
        """Test case for create_priority_class

        """
        pass

    def test_delete_collection_priority_class(self):
        """Test case for delete_collection_priority_class

        """
        pass

    def test_delete_priority_class(self):
        """Test case for delete_priority_class

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_priority_class(self):
        """Test case for list_priority_class

        """
        pass

    def test_patch_priority_class(self):
        """Test case for patch_priority_class

        """
        pass

    def test_read_priority_class(self):
        """Test case for read_priority_class

        """
        pass

    def test_replace_priority_class(self):
        """Test case for replace_priority_class

        """
        pass


if __name__ == '__main__':
    unittest.main()
