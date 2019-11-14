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
from swagger_client.models.embed_playbook_step_completed import EmbedPlaybookStepCompleted  # noqa: F401,E501
from swagger_client.models.embed_playbook_step_execution import EmbedPlaybookStepExecution  # noqa: F401,E501
from swagger_client.models.observable_owner import ObservableOwner  # noqa: F401,E501


class EmbedPlaybookStep(object):
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
        'explanation': 'str',
        'id': 'str',
        'depth': 'str',
        'execution': 'list[EmbedPlaybookStepExecution]',
        'completed': 'list[EmbedPlaybookStepCompleted]',
        'assigned_to': 'ObservableOwner',
        'due_date': 'date'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'method': 'method',
        'type': 'type',
        'automation': 'automation',
        'explanation': 'explanation',
        'id': 'id',
        'depth': 'depth',
        'execution': 'execution',
        'completed': 'completed',
        'assigned_to': 'assignedTo',
        'due_date': 'dueDate'
    }

    def __init__(self, name=None, description=None, method=None, type=None, automation=None, explanation=None, id=None, depth=None, execution=None, completed=None, assigned_to=None, due_date=None):  # noqa: E501
        """EmbedPlaybookStep - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._method = None
        self._type = None
        self._automation = None
        self._explanation = None
        self._id = None
        self._depth = None
        self._execution = None
        self._completed = None
        self._assigned_to = None
        self._due_date = None
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
        if id is not None:
            self.id = id
        if depth is not None:
            self.depth = depth
        if execution is not None:
            self.execution = execution
        if completed is not None:
            self.completed = completed
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if due_date is not None:
            self.due_date = due_date

    @property
    def name(self):
        """Gets the name of this EmbedPlaybookStep.  # noqa: E501


        :return: The name of this EmbedPlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmbedPlaybookStep.


        :param name: The name of this EmbedPlaybookStep.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this EmbedPlaybookStep.  # noqa: E501


        :return: The description of this EmbedPlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EmbedPlaybookStep.


        :param description: The description of this EmbedPlaybookStep.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def method(self):
        """Gets the method of this EmbedPlaybookStep.  # noqa: E501


        :return: The method of this EmbedPlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this EmbedPlaybookStep.


        :param method: The method of this EmbedPlaybookStep.  # noqa: E501
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
        """Gets the type of this EmbedPlaybookStep.  # noqa: E501


        :return: The type of this EmbedPlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmbedPlaybookStep.


        :param type: The type of this EmbedPlaybookStep.  # noqa: E501
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
        """Gets the automation of this EmbedPlaybookStep.  # noqa: E501


        :return: The automation of this EmbedPlaybookStep.  # noqa: E501
        :rtype: EmbedPlaybookStepAutomation
        """
        return self._automation

    @automation.setter
    def automation(self, automation):
        """Sets the automation of this EmbedPlaybookStep.


        :param automation: The automation of this EmbedPlaybookStep.  # noqa: E501
        :type: EmbedPlaybookStepAutomation
        """

        self._automation = automation

    @property
    def explanation(self):
        """Gets the explanation of this EmbedPlaybookStep.  # noqa: E501

        Explanation of possible results  # noqa: E501

        :return: The explanation of this EmbedPlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """Sets the explanation of this EmbedPlaybookStep.

        Explanation of possible results  # noqa: E501

        :param explanation: The explanation of this EmbedPlaybookStep.  # noqa: E501
        :type: str
        """

        self._explanation = explanation

    @property
    def id(self):
        """Gets the id of this EmbedPlaybookStep.  # noqa: E501


        :return: The id of this EmbedPlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmbedPlaybookStep.


        :param id: The id of this EmbedPlaybookStep.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def depth(self):
        """Gets the depth of this EmbedPlaybookStep.  # noqa: E501

        Playbook step nesting  # noqa: E501

        :return: The depth of this EmbedPlaybookStep.  # noqa: E501
        :rtype: str
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this EmbedPlaybookStep.

        Playbook step nesting  # noqa: E501

        :param depth: The depth of this EmbedPlaybookStep.  # noqa: E501
        :type: str
        """

        self._depth = depth

    @property
    def execution(self):
        """Gets the execution of this EmbedPlaybookStep.  # noqa: E501

        Execution data (only for automated steps)  # noqa: E501

        :return: The execution of this EmbedPlaybookStep.  # noqa: E501
        :rtype: list[EmbedPlaybookStepExecution]
        """
        return self._execution

    @execution.setter
    def execution(self, execution):
        """Sets the execution of this EmbedPlaybookStep.

        Execution data (only for automated steps)  # noqa: E501

        :param execution: The execution of this EmbedPlaybookStep.  # noqa: E501
        :type: list[EmbedPlaybookStepExecution]
        """

        self._execution = execution

    @property
    def completed(self):
        """Gets the completed of this EmbedPlaybookStep.  # noqa: E501

        Completed data of playbook step  # noqa: E501

        :return: The completed of this EmbedPlaybookStep.  # noqa: E501
        :rtype: list[EmbedPlaybookStepCompleted]
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this EmbedPlaybookStep.

        Completed data of playbook step  # noqa: E501

        :param completed: The completed of this EmbedPlaybookStep.  # noqa: E501
        :type: list[EmbedPlaybookStepCompleted]
        """

        self._completed = completed

    @property
    def assigned_to(self):
        """Gets the assigned_to of this EmbedPlaybookStep.  # noqa: E501


        :return: The assigned_to of this EmbedPlaybookStep.  # noqa: E501
        :rtype: ObservableOwner
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this EmbedPlaybookStep.


        :param assigned_to: The assigned_to of this EmbedPlaybookStep.  # noqa: E501
        :type: ObservableOwner
        """

        self._assigned_to = assigned_to

    @property
    def due_date(self):
        """Gets the due_date of this EmbedPlaybookStep.  # noqa: E501


        :return: The due_date of this EmbedPlaybookStep.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this EmbedPlaybookStep.


        :param due_date: The due_date of this EmbedPlaybookStep.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

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
        if not isinstance(other, EmbedPlaybookStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
