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


class V1FlockerVolumeSource(object):
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
        'dataset_name': 'str',
        'dataset_uuid': 'str'
    }

    attribute_map = {
        'dataset_name': 'datasetName',
        'dataset_uuid': 'datasetUUID'
    }

    def __init__(self, dataset_name=None, dataset_uuid=None):  # noqa: E501
        """V1FlockerVolumeSource - a model defined in OpenAPI"""  # noqa: E501

        self._dataset_name = None
        self._dataset_uuid = None
        self.discriminator = None

        if dataset_name is not None:
            self.dataset_name = dataset_name
        if dataset_uuid is not None:
            self.dataset_uuid = dataset_uuid

    @property
    def dataset_name(self):
        """Gets the dataset_name of this V1FlockerVolumeSource.  # noqa: E501

        Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated  # noqa: E501

        :return: The dataset_name of this V1FlockerVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        """Sets the dataset_name of this V1FlockerVolumeSource.

        Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated  # noqa: E501

        :param dataset_name: The dataset_name of this V1FlockerVolumeSource.  # noqa: E501
        :type: str
        """

        self._dataset_name = dataset_name

    @property
    def dataset_uuid(self):
        """Gets the dataset_uuid of this V1FlockerVolumeSource.  # noqa: E501

        UUID of the dataset. This is unique identifier of a Flocker dataset  # noqa: E501

        :return: The dataset_uuid of this V1FlockerVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._dataset_uuid

    @dataset_uuid.setter
    def dataset_uuid(self, dataset_uuid):
        """Sets the dataset_uuid of this V1FlockerVolumeSource.

        UUID of the dataset. This is unique identifier of a Flocker dataset  # noqa: E501

        :param dataset_uuid: The dataset_uuid of this V1FlockerVolumeSource.  # noqa: E501
        :type: str
        """

        self._dataset_uuid = dataset_uuid

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
        if not isinstance(other, V1FlockerVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
