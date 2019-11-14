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

from swagger_client.models.embed_playbook_step_started_by import EmbedPlaybookStepStartedBy  # noqa: F401,E501


class EmbedPlaybookStepExecution(object):
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
        'result': 'str',
        'modified': 'date',
        'started_by': 'EmbedPlaybookStepStartedBy'
    }

    attribute_map = {
        'status': 'status',
        'result': 'result',
        'modified': 'modified',
        'started_by': 'startedBy'
    }

    def __init__(self, status=None, result=None, modified=None, started_by=None):  # noqa: E501
        """EmbedPlaybookStepExecution - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._result = None
        self._modified = None
        self._started_by = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if result is not None:
            self.result = result
        if modified is not None:
            self.modified = modified
        if started_by is not None:
            self.started_by = started_by

    @property
    def status(self):
        """Gets the status of this EmbedPlaybookStepExecution.  # noqa: E501

        Status of execution  # noqa: E501

        :return: The status of this EmbedPlaybookStepExecution.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EmbedPlaybookStepExecution.

        Status of execution  # noqa: E501

        :param status: The status of this EmbedPlaybookStepExecution.  # noqa: E501
        :type: str
        """
        allowed_values = ["failed", "running", "succeed", "error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def result(self):
        """Gets the result of this EmbedPlaybookStepExecution.  # noqa: E501

        Result message id  # noqa: E501

        :return: The result of this EmbedPlaybookStepExecution.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this EmbedPlaybookStepExecution.

        Result message id  # noqa: E501

        :param result: The result of this EmbedPlaybookStepExecution.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def modified(self):
        """Gets the modified of this EmbedPlaybookStepExecution.  # noqa: E501


        :return: The modified of this EmbedPlaybookStepExecution.  # noqa: E501
        :rtype: date
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this EmbedPlaybookStepExecution.


        :param modified: The modified of this EmbedPlaybookStepExecution.  # noqa: E501
        :type: date
        """

        self._modified = modified

    @property
    def started_by(self):
        """Gets the started_by of this EmbedPlaybookStepExecution.  # noqa: E501


        :return: The started_by of this EmbedPlaybookStepExecution.  # noqa: E501
        :rtype: EmbedPlaybookStepStartedBy
        """
        return self._started_by

    @started_by.setter
    def started_by(self, started_by):
        """Sets the started_by of this EmbedPlaybookStepExecution.


        :param started_by: The started_by of this EmbedPlaybookStepExecution.  # noqa: E501
        :type: EmbedPlaybookStepStartedBy
        """

        self._started_by = started_by

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
        if not isinstance(other, EmbedPlaybookStepExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
