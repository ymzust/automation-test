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

from swagger_client.models.dashboard_assigned_recent_incidents import DashboardAssignedRecentIncidents  # noqa: F401,E501


class DashboardAssigned(object):
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
        'assigned_actions': 'list[str]',
        'recent_incidents': 'list[DashboardAssignedRecentIncidents]'
    }

    attribute_map = {
        'assigned_actions': 'assignedActions',
        'recent_incidents': 'recentIncidents'
    }

    def __init__(self, assigned_actions=None, recent_incidents=None):  # noqa: E501
        """DashboardAssigned - a model defined in Swagger"""  # noqa: E501

        self._assigned_actions = None
        self._recent_incidents = None
        self.discriminator = None

        if assigned_actions is not None:
            self.assigned_actions = assigned_actions
        if recent_incidents is not None:
            self.recent_incidents = recent_incidents

    @property
    def assigned_actions(self):
        """Gets the assigned_actions of this DashboardAssigned.  # noqa: E501


        :return: The assigned_actions of this DashboardAssigned.  # noqa: E501
        :rtype: list[str]
        """
        return self._assigned_actions

    @assigned_actions.setter
    def assigned_actions(self, assigned_actions):
        """Sets the assigned_actions of this DashboardAssigned.


        :param assigned_actions: The assigned_actions of this DashboardAssigned.  # noqa: E501
        :type: list[str]
        """

        self._assigned_actions = assigned_actions

    @property
    def recent_incidents(self):
        """Gets the recent_incidents of this DashboardAssigned.  # noqa: E501


        :return: The recent_incidents of this DashboardAssigned.  # noqa: E501
        :rtype: list[DashboardAssignedRecentIncidents]
        """
        return self._recent_incidents

    @recent_incidents.setter
    def recent_incidents(self, recent_incidents):
        """Sets the recent_incidents of this DashboardAssigned.


        :param recent_incidents: The recent_incidents of this DashboardAssigned.  # noqa: E501
        :type: list[DashboardAssignedRecentIncidents]
        """

        self._recent_incidents = recent_incidents

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
        if not isinstance(other, DashboardAssigned):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other