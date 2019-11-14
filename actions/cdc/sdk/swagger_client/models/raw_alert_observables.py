# coding: utf-8

"""
    CyberProof Platform Backend API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RawAlertObservables(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'labels': 'list[str]',
        'id': 'str'
    }

    attribute_map = {
        'labels': 'labels',
        'id': '_id'
    }

    def __init__(self, labels=None, id=None):  # noqa: E501
        """RawAlertObservables - a model defined in Swagger"""  # noqa: E501

        self._labels = None
        self._id = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels
        if id is not None:
            self.id = id

    @property
    def labels(self):
        """Gets the labels of this RawAlertObservables.  # noqa: E501


        :return: The labels of this RawAlertObservables.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this RawAlertObservables.


        :param labels: The labels of this RawAlertObservables.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def id(self):
        """Gets the id of this RawAlertObservables.  # noqa: E501


        :return: The id of this RawAlertObservables.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RawAlertObservables.


        :param id: The id of this RawAlertObservables.  # noqa: E501
        :type: str
        """

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, RawAlertObservables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
