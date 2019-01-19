# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.12.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1NonResourceRule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'non_resource_ur_ls': 'list[str]',
        'verbs': 'list[str]'
    }

    attribute_map = {
        'non_resource_ur_ls': 'nonResourceURLs',
        'verbs': 'verbs'
    }

    def __init__(self, non_resource_ur_ls=None, verbs=None):  # noqa: E501
        """V1NonResourceRule - a model defined in OpenAPI"""  # noqa: E501

        self._non_resource_ur_ls = None
        self._verbs = None
        self.discriminator = None

        if non_resource_ur_ls is not None:
            self.non_resource_ur_ls = non_resource_ur_ls
        self.verbs = verbs

    @property
    def non_resource_ur_ls(self):
        """Gets the non_resource_ur_ls of this V1NonResourceRule.  # noqa: E501

        NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  \"*\" means all.  # noqa: E501

        :return: The non_resource_ur_ls of this V1NonResourceRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._non_resource_ur_ls

    @non_resource_ur_ls.setter
    def non_resource_ur_ls(self, non_resource_ur_ls):
        """Sets the non_resource_ur_ls of this V1NonResourceRule.

        NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  \"*\" means all.  # noqa: E501

        :param non_resource_ur_ls: The non_resource_ur_ls of this V1NonResourceRule.  # noqa: E501
        :type: list[str]
        """

        self._non_resource_ur_ls = non_resource_ur_ls

    @property
    def verbs(self):
        """Gets the verbs of this V1NonResourceRule.  # noqa: E501

        Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  \"*\" means all.  # noqa: E501

        :return: The verbs of this V1NonResourceRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """Sets the verbs of this V1NonResourceRule.

        Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  \"*\" means all.  # noqa: E501

        :param verbs: The verbs of this V1NonResourceRule.  # noqa: E501
        :type: list[str]
        """
        if verbs is None:
            raise ValueError("Invalid value for `verbs`, must not be `None`")  # noqa: E501

        self._verbs = verbs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1NonResourceRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
