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


class ExtensionsV1beta1SELinuxStrategyOptions(object):
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
        'rule': 'str',
        'se_linux_options': 'V1SELinuxOptions'
    }

    attribute_map = {
        'rule': 'rule',
        'se_linux_options': 'seLinuxOptions'
    }

    def __init__(self, rule=None, se_linux_options=None):  # noqa: E501
        """ExtensionsV1beta1SELinuxStrategyOptions - a model defined in OpenAPI"""  # noqa: E501

        self._rule = None
        self._se_linux_options = None
        self.discriminator = None

        self.rule = rule
        if se_linux_options is not None:
            self.se_linux_options = se_linux_options

    @property
    def rule(self):
        """Gets the rule of this ExtensionsV1beta1SELinuxStrategyOptions.  # noqa: E501

        rule is the strategy that will dictate the allowable labels that may be set.  # noqa: E501

        :return: The rule of this ExtensionsV1beta1SELinuxStrategyOptions.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ExtensionsV1beta1SELinuxStrategyOptions.

        rule is the strategy that will dictate the allowable labels that may be set.  # noqa: E501

        :param rule: The rule of this ExtensionsV1beta1SELinuxStrategyOptions.  # noqa: E501
        :type: str
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501

        self._rule = rule

    @property
    def se_linux_options(self):
        """Gets the se_linux_options of this ExtensionsV1beta1SELinuxStrategyOptions.  # noqa: E501


        :return: The se_linux_options of this ExtensionsV1beta1SELinuxStrategyOptions.  # noqa: E501
        :rtype: V1SELinuxOptions
        """
        return self._se_linux_options

    @se_linux_options.setter
    def se_linux_options(self, se_linux_options):
        """Sets the se_linux_options of this ExtensionsV1beta1SELinuxStrategyOptions.


        :param se_linux_options: The se_linux_options of this ExtensionsV1beta1SELinuxStrategyOptions.  # noqa: E501
        :type: V1SELinuxOptions
        """

        self._se_linux_options = se_linux_options

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
        if not isinstance(other, ExtensionsV1beta1SELinuxStrategyOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
