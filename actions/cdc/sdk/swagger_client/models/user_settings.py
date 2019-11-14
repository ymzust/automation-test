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

from swagger_client.models.user_settings_alert import UserSettingsAlert  # noqa: F401,E501


class UserSettings(object):
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
        'alert': 'UserSettingsAlert'
    }

    attribute_map = {
        'alert': 'alert'
    }

    def __init__(self, alert=None):  # noqa: E501
        """UserSettings - a model defined in Swagger"""  # noqa: E501

        self._alert = None
        self.discriminator = None

        if alert is not None:
            self.alert = alert

    @property
    def alert(self):
        """Gets the alert of this UserSettings.  # noqa: E501


        :return: The alert of this UserSettings.  # noqa: E501
        :rtype: UserSettingsAlert
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """Sets the alert of this UserSettings.


        :param alert: The alert of this UserSettings.  # noqa: E501
        :type: UserSettingsAlert
        """

        self._alert = alert

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
        if not isinstance(other, UserSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
