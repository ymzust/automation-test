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


class ObservableEnrichment(object):
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
        'status': 'str',
        'type': 'str',
        'ioc': 'bool',
        'is_history': 'bool',
        'result': 'object',
        'created': 'date',
        'modified': 'date'
    }

    attribute_map = {
        'id': '_id',
        'status': 'status',
        'type': 'type',
        'ioc': 'ioc',
        'is_history': 'isHistory',
        'result': 'result',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, id=None, status=None, type=None, ioc=None, is_history=None, result=None, created=None, modified=None):  # noqa: E501
        """ObservableEnrichment - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._status = None
        self._type = None
        self._ioc = None
        self._is_history = None
        self._result = None
        self._created = None
        self._modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if ioc is not None:
            self.ioc = ioc
        if is_history is not None:
            self.is_history = is_history
        if result is not None:
            self.result = result
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified

    @property
    def id(self):
        """Gets the id of this ObservableEnrichment.  # noqa: E501


        :return: The id of this ObservableEnrichment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObservableEnrichment.


        :param id: The id of this ObservableEnrichment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this ObservableEnrichment.  # noqa: E501


        :return: The status of this ObservableEnrichment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ObservableEnrichment.


        :param status: The status of this ObservableEnrichment.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this ObservableEnrichment.  # noqa: E501


        :return: The type of this ObservableEnrichment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ObservableEnrichment.


        :param type: The type of this ObservableEnrichment.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def ioc(self):
        """Gets the ioc of this ObservableEnrichment.  # noqa: E501


        :return: The ioc of this ObservableEnrichment.  # noqa: E501
        :rtype: bool
        """
        return self._ioc

    @ioc.setter
    def ioc(self, ioc):
        """Sets the ioc of this ObservableEnrichment.


        :param ioc: The ioc of this ObservableEnrichment.  # noqa: E501
        :type: bool
        """

        self._ioc = ioc

    @property
    def is_history(self):
        """Gets the is_history of this ObservableEnrichment.  # noqa: E501


        :return: The is_history of this ObservableEnrichment.  # noqa: E501
        :rtype: bool
        """
        return self._is_history

    @is_history.setter
    def is_history(self, is_history):
        """Sets the is_history of this ObservableEnrichment.


        :param is_history: The is_history of this ObservableEnrichment.  # noqa: E501
        :type: bool
        """

        self._is_history = is_history

    @property
    def result(self):
        """Gets the result of this ObservableEnrichment.  # noqa: E501


        :return: The result of this ObservableEnrichment.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ObservableEnrichment.


        :param result: The result of this ObservableEnrichment.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def created(self):
        """Gets the created of this ObservableEnrichment.  # noqa: E501


        :return: The created of this ObservableEnrichment.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ObservableEnrichment.


        :param created: The created of this ObservableEnrichment.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this ObservableEnrichment.  # noqa: E501


        :return: The modified of this ObservableEnrichment.  # noqa: E501
        :rtype: date
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ObservableEnrichment.


        :param modified: The modified of this ObservableEnrichment.  # noqa: E501
        :type: date
        """

        self._modified = modified

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
        if not isinstance(other, ObservableEnrichment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other