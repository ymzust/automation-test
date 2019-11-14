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

from swagger_client.models.embed_playbook_step_automation import EmbedPlaybookStepAutomation  # noqa: F401,E501


class PlaybookStep(object):
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
        'name': 'str',
        'description': 'str',
        'method': 'str',
        'type': 'str',
        'automation': 'EmbedPlaybookStepAutomation',
        'explanation': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'method': 'method',
        'type': 'type',
        'automation': 'automation',
        'explanation': 'explanation'
    }

    def __init__(self, name=None, description=None, method=None, type=None, automation=None, explanation=None):  # noqa: E501
        """PlaybookStep - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._method = None
        self._type = None
        self._automation = None
        self._explanation = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.method = method
        self.type = type
        if automation is not None:
            self.automation = automation
        if explanation is not None:
            self.explanation = explanation

    @property
    def name(self):
        """Gets the name of this PlaybookStep.  # noqa: E501


        :return: The name of this PlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlaybookStep.


        :param name: The name of this PlaybookStep.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this PlaybookStep.  # noqa: E501


        :return: The description of this PlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PlaybookStep.


        :param description: The description of this PlaybookStep.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def method(self):
        """Gets the method of this PlaybookStep.  # noqa: E501


        :return: The method of this PlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this PlaybookStep.


        :param method: The method of this PlaybookStep.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["manual", "auto", "script"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def type(self):
        """Gets the type of this PlaybookStep.  # noqa: E501


        :return: The type of this PlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PlaybookStep.


        :param type: The type of this PlaybookStep.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["block", "condition"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def automation(self):
        """Gets the automation of this PlaybookStep.  # noqa: E501


        :return: The automation of this PlaybookStep.  # noqa: E501
        :rtype: EmbedPlaybookStepAutomation
        """
        return self._automation

    @automation.setter
    def automation(self, automation):
        """Sets the automation of this PlaybookStep.


        :param automation: The automation of this PlaybookStep.  # noqa: E501
        :type: EmbedPlaybookStepAutomation
        """

        self._automation = automation

    @property
    def explanation(self):
        """Gets the explanation of this PlaybookStep.  # noqa: E501

        Explanation of possible results  # noqa: E501

        :return: The explanation of this PlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """Sets the explanation of this PlaybookStep.

        Explanation of possible results  # noqa: E501

        :param explanation: The explanation of this PlaybookStep.  # noqa: E501
        :type: str
        """

        self._explanation = explanation

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
        if not isinstance(other, PlaybookStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other