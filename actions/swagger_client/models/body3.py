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


class Body3(object):
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
        'status': 'str',
        'ioc': 'bool',
        'result': 'object'
    }

    attribute_map = {
        'status': 'status',
        'ioc': 'ioc',
        'result': 'result'
    }

    def __init__(self, status=None, ioc=None, result=None):  # noqa: E501
        """Body3 - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._ioc = None
        self._result = None
        self.discriminator = None

        self.status = status
        if ioc is not None:
            self.ioc = ioc
        if result is not None:
            self.result = result

    @property
    def status(self):
        """Gets the status of this Body3.  # noqa: E501


        :return: The status of this Body3.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Body3.


        :param status: The status of this Body3.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def ioc(self):
        """Gets the ioc of this Body3.  # noqa: E501


        :return: The ioc of this Body3.  # noqa: E501
        :rtype: bool
        """
        return self._ioc

    @ioc.setter
    def ioc(self, ioc):
        """Sets the ioc of this Body3.


        :param ioc: The ioc of this Body3.  # noqa: E501
        :type: bool
        """

        self._ioc = ioc

    @property
    def result(self):
        """Gets the result of this Body3.  # noqa: E501


        :return: The result of this Body3.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Body3.


        :param result: The result of this Body3.  # noqa: E501
        :type: object
        """

        self._result = result

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
        if not isinstance(other, Body3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
