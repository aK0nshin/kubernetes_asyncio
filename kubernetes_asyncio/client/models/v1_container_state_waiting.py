# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.12.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1ContainerStateWaiting(object):
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
        'message': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'message': 'message',
        'reason': 'reason'
    }

    def __init__(self, message=None, reason=None):  # noqa: E501
        """V1ContainerStateWaiting - a model defined in OpenAPI"""  # noqa: E501

        self._message = None
        self._reason = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason

    @property
    def message(self):
        """Gets the message of this V1ContainerStateWaiting.  # noqa: E501

        Message regarding why the container is not yet running.  # noqa: E501

        :return: The message of this V1ContainerStateWaiting.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1ContainerStateWaiting.

        Message regarding why the container is not yet running.  # noqa: E501

        :param message: The message of this V1ContainerStateWaiting.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this V1ContainerStateWaiting.  # noqa: E501

        (brief) reason the container is not yet running.  # noqa: E501

        :return: The reason of this V1ContainerStateWaiting.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1ContainerStateWaiting.

        (brief) reason the container is not yet running.  # noqa: E501

        :param reason: The reason of this V1ContainerStateWaiting.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if not isinstance(other, V1ContainerStateWaiting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
