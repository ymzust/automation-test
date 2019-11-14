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

from swagger_client.models.cpp_alert_device import CppAlertDevice  # noqa: F401,E501
from swagger_client.models.cpp_alert_observables import CppAlertObservables  # noqa: F401,E501


class CppAlertEvents(object):
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
        'event_id': 'float',
        'event_time': 'str',
        'name': 'str',
        'device': 'CppAlertDevice',
        'observables': 'list[CppAlertObservables]'
    }

    attribute_map = {
        'event_id': 'eventId',
        'event_time': 'eventTime',
        'name': 'name',
        'device': 'device',
        'observables': 'observables'
    }

    def __init__(self, event_id=None, event_time=None, name=None, device=None, observables=None):  # noqa: E501
        """CppAlertEvents - a model defined in Swagger"""  # noqa: E501

        self._event_id = None
        self._event_time = None
        self._name = None
        self._device = None
        self._observables = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if event_time is not None:
            self.event_time = event_time
        if name is not None:
            self.name = name
        if device is not None:
            self.device = device
        if observables is not None:
            self.observables = observables

    @property
    def event_id(self):
        """Gets the event_id of this CppAlertEvents.  # noqa: E501


        :return: The event_id of this CppAlertEvents.  # noqa: E501
        :rtype: float
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this CppAlertEvents.


        :param event_id: The event_id of this CppAlertEvents.  # noqa: E501
        :type: float
        """

        self._event_id = event_id

    @property
    def event_time(self):
        """Gets the event_time of this CppAlertEvents.  # noqa: E501


        :return: The event_time of this CppAlertEvents.  # noqa: E501
        :rtype: str
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this CppAlertEvents.


        :param event_time: The event_time of this CppAlertEvents.  # noqa: E501
        :type: str
        """

        self._event_time = event_time

    @property
    def name(self):
        """Gets the name of this CppAlertEvents.  # noqa: E501


        :return: The name of this CppAlertEvents.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CppAlertEvents.


        :param name: The name of this CppAlertEvents.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def device(self):
        """Gets the device of this CppAlertEvents.  # noqa: E501


        :return: The device of this CppAlertEvents.  # noqa: E501
        :rtype: CppAlertDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this CppAlertEvents.


        :param device: The device of this CppAlertEvents.  # noqa: E501
        :type: CppAlertDevice
        """

        self._device = device

    @property
    def observables(self):
        """Gets the observables of this CppAlertEvents.  # noqa: E501


        :return: The observables of this CppAlertEvents.  # noqa: E501
        :rtype: list[CppAlertObservables]
        """
        return self._observables

    @observables.setter
    def observables(self, observables):
        """Sets the observables of this CppAlertEvents.


        :param observables: The observables of this CppAlertEvents.  # noqa: E501
        :type: list[CppAlertObservables]
        """

        self._observables = observables

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
        if not isinstance(other, CppAlertEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
