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


class IncidentEvidenceItem(object):
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
        'type': 'str',
        'reference_id': 'str'
    }

    attribute_map = {
        'id': '_id',
        'type': 'type',
        'reference_id': 'referenceId'
    }

    def __init__(self, id=None, type='evidence', reference_id=None):  # noqa: E501
        """IncidentEvidenceItem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._reference_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if reference_id is not None:
            self.reference_id = reference_id

    @property
    def id(self):
        """Gets the id of this IncidentEvidenceItem.  # noqa: E501


        :return: The id of this IncidentEvidenceItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncidentEvidenceItem.


        :param id: The id of this IncidentEvidenceItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this IncidentEvidenceItem.  # noqa: E501


        :return: The type of this IncidentEvidenceItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IncidentEvidenceItem.


        :param type: The type of this IncidentEvidenceItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["evidence"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def reference_id(self):
        """Gets the reference_id of this IncidentEvidenceItem.  # noqa: E501


        :return: The reference_id of this IncidentEvidenceItem.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this IncidentEvidenceItem.


        :param reference_id: The reference_id of this IncidentEvidenceItem.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

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
        if not isinstance(other, IncidentEvidenceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other