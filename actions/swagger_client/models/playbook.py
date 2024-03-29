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

from swagger_client.models.playbook_edges import PlaybookEdges  # noqa: F401,E501
from swagger_client.models.playbook_step import PlaybookStep  # noqa: F401,E501


class Playbook(object):
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
        'organization': 'str',
        'name': 'str',
        'types': 'list[str]',
        'tags': 'list[str]',
        'nodes': 'list[PlaybookStep]',
        'edges': 'list[PlaybookEdges]'
    }

    attribute_map = {
        'id': '_id',
        'organization': 'organization',
        'name': 'name',
        'types': 'types',
        'tags': 'tags',
        'nodes': 'nodes',
        'edges': 'edges'
    }

    def __init__(self, id=None, organization=None, name=None, types=None, tags=None, nodes=None, edges=None):  # noqa: E501
        """Playbook - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._organization = None
        self._name = None
        self._types = None
        self._tags = None
        self._nodes = None
        self._edges = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if organization is not None:
            self.organization = organization
        self.name = name
        if types is not None:
            self.types = types
        if tags is not None:
            self.tags = tags
        self.nodes = nodes
        if edges is not None:
            self.edges = edges

    @property
    def id(self):
        """Gets the id of this Playbook.  # noqa: E501


        :return: The id of this Playbook.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Playbook.


        :param id: The id of this Playbook.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organization(self):
        """Gets the organization of this Playbook.  # noqa: E501


        :return: The organization of this Playbook.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Playbook.


        :param organization: The organization of this Playbook.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def name(self):
        """Gets the name of this Playbook.  # noqa: E501


        :return: The name of this Playbook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Playbook.


        :param name: The name of this Playbook.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def types(self):
        """Gets the types of this Playbook.  # noqa: E501

        Values from metamodels (incident type)  # noqa: E501

        :return: The types of this Playbook.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this Playbook.

        Values from metamodels (incident type)  # noqa: E501

        :param types: The types of this Playbook.  # noqa: E501
        :type: list[str]
        """

        self._types = types

    @property
    def tags(self):
        """Gets the tags of this Playbook.  # noqa: E501


        :return: The tags of this Playbook.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Playbook.


        :param tags: The tags of this Playbook.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def nodes(self):
        """Gets the nodes of this Playbook.  # noqa: E501


        :return: The nodes of this Playbook.  # noqa: E501
        :rtype: list[PlaybookStep]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this Playbook.


        :param nodes: The nodes of this Playbook.  # noqa: E501
        :type: list[PlaybookStep]
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        self._nodes = nodes

    @property
    def edges(self):
        """Gets the edges of this Playbook.  # noqa: E501


        :return: The edges of this Playbook.  # noqa: E501
        :rtype: list[PlaybookEdges]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this Playbook.


        :param edges: The edges of this Playbook.  # noqa: E501
        :type: list[PlaybookEdges]
        """

        self._edges = edges

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
        if not isinstance(other, Playbook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
