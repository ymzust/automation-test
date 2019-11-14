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

from swagger_client.models.observable_owner import ObservableOwner  # noqa: F401,E501


class ObservableDetails(object):
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
        'key': 'str',
        'value': 'str',
        'created_date': 'date',
        'end_date': 'date',
        'owner': 'ObservableOwner',
        'source': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'created_date': 'createdDate',
        'end_date': 'endDate',
        'owner': 'owner',
        'source': 'source'
    }

    def __init__(self, key=None, value=None, created_date=None, end_date=None, owner=None, source=None):  # noqa: E501
        """ObservableDetails - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._value = None
        self._created_date = None
        self._end_date = None
        self._owner = None
        self._source = None
        self.discriminator = None

        self.key = key
        self.value = value
        if created_date is not None:
            self.created_date = created_date
        if end_date is not None:
            self.end_date = end_date
        if owner is not None:
            self.owner = owner
        self.source = source

    @property
    def key(self):
        """Gets the key of this ObservableDetails.  # noqa: E501


        :return: The key of this ObservableDetails.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ObservableDetails.


        :param key: The key of this ObservableDetails.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this ObservableDetails.  # noqa: E501


        :return: The value of this ObservableDetails.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ObservableDetails.


        :param value: The value of this ObservableDetails.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def created_date(self):
        """Gets the created_date of this ObservableDetails.  # noqa: E501


        :return: The created_date of this ObservableDetails.  # noqa: E501
        :rtype: date
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ObservableDetails.


        :param created_date: The created_date of this ObservableDetails.  # noqa: E501
        :type: date
        """

        self._created_date = created_date

    @property
    def end_date(self):
        """Gets the end_date of this ObservableDetails.  # noqa: E501


        :return: The end_date of this ObservableDetails.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ObservableDetails.


        :param end_date: The end_date of this ObservableDetails.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def owner(self):
        """Gets the owner of this ObservableDetails.  # noqa: E501


        :return: The owner of this ObservableDetails.  # noqa: E501
        :rtype: ObservableOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ObservableDetails.


        :param owner: The owner of this ObservableDetails.  # noqa: E501
        :type: ObservableOwner
        """

        self._owner = owner

    @property
    def source(self):
        """Gets the source of this ObservableDetails.  # noqa: E501


        :return: The source of this ObservableDetails.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ObservableDetails.


        :param source: The source of this ObservableDetails.  # noqa: E501
        :type: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

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
        if not isinstance(other, ObservableDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other