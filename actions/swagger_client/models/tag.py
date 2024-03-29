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


class Tag(object):
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
        'id': 'str',
        'value': 'str',
        'organization': 'str',
        'created': 'date',
        'modified': 'date',
        'number_of_incidents': 'int',
        'number_of_observables': 'str'
    }

    attribute_map = {
        'id': '_id',
        'value': 'value',
        'organization': 'organization',
        'created': 'created',
        'modified': 'modified',
        'number_of_incidents': 'numberOfIncidents',
        'number_of_observables': 'numberOfObservables'
    }

    def __init__(self, id=None, value=None, organization=None, created=None, modified=None, number_of_incidents=None, number_of_observables=None):  # noqa: E501
        """Tag - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._value = None
        self._organization = None
        self._created = None
        self._modified = None
        self._number_of_incidents = None
        self._number_of_observables = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.value = value
        if organization is not None:
            self.organization = organization
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if number_of_incidents is not None:
            self.number_of_incidents = number_of_incidents
        if number_of_observables is not None:
            self.number_of_observables = number_of_observables

    @property
    def id(self):
        """Gets the id of this Tag.  # noqa: E501


        :return: The id of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tag.


        :param id: The id of this Tag.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this Tag.  # noqa: E501


        :return: The value of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Tag.


        :param value: The value of this Tag.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def organization(self):
        """Gets the organization of this Tag.  # noqa: E501


        :return: The organization of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Tag.


        :param organization: The organization of this Tag.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def created(self):
        """Gets the created of this Tag.  # noqa: E501


        :return: The created of this Tag.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Tag.


        :param created: The created of this Tag.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Tag.  # noqa: E501


        :return: The modified of this Tag.  # noqa: E501
        :rtype: date
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Tag.


        :param modified: The modified of this Tag.  # noqa: E501
        :type: date
        """

        self._modified = modified

    @property
    def number_of_incidents(self):
        """Gets the number_of_incidents of this Tag.  # noqa: E501

        Property present only in list  # noqa: E501

        :return: The number_of_incidents of this Tag.  # noqa: E501
        :rtype: int
        """
        return self._number_of_incidents

    @number_of_incidents.setter
    def number_of_incidents(self, number_of_incidents):
        """Sets the number_of_incidents of this Tag.

        Property present only in list  # noqa: E501

        :param number_of_incidents: The number_of_incidents of this Tag.  # noqa: E501
        :type: int
        """

        self._number_of_incidents = number_of_incidents

    @property
    def number_of_observables(self):
        """Gets the number_of_observables of this Tag.  # noqa: E501

        Property present only in list  # noqa: E501

        :return: The number_of_observables of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._number_of_observables

    @number_of_observables.setter
    def number_of_observables(self, number_of_observables):
        """Sets the number_of_observables of this Tag.

        Property present only in list  # noqa: E501

        :param number_of_observables: The number_of_observables of this Tag.  # noqa: E501
        :type: str
        """

        self._number_of_observables = number_of_observables

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
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
