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


class Body23(object):
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
        'trigger': 'str',
        'url': 'str',
        'name': 'str'
    }

    attribute_map = {
        'trigger': 'trigger',
        'url': 'url',
        'name': 'name'
    }

    def __init__(self, trigger='channel:update', url=None, name=None):  # noqa: E501
        """Body23 - a model defined in Swagger"""  # noqa: E501

        self._trigger = None
        self._url = None
        self._name = None
        self.discriminator = None

        if trigger is not None:
            self.trigger = trigger
        if url is not None:
            self.url = url
        if name is not None:
            self.name = name

    @property
    def trigger(self):
        """Gets the trigger of this Body23.  # noqa: E501

        trigger  # noqa: E501

        :return: The trigger of this Body23.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this Body23.

        trigger  # noqa: E501

        :param trigger: The trigger of this Body23.  # noqa: E501
        :type: str
        """

        self._trigger = trigger

    @property
    def url(self):
        """Gets the url of this Body23.  # noqa: E501

        url  # noqa: E501

        :return: The url of this Body23.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Body23.

        url  # noqa: E501

        :param url: The url of this Body23.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this Body23.  # noqa: E501

        name  # noqa: E501

        :return: The name of this Body23.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body23.

        name  # noqa: E501

        :param name: The name of this Body23.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Body23):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other