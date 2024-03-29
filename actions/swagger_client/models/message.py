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

from swagger_client.models.channel_users import ChannelUsers  # noqa: F401,E501
from swagger_client.models.incident_external_id_message_attachment import IncidentExternalIdMessageAttachment  # noqa: F401,E501
from swagger_client.models.message_thread_comment import MessageThreadComment  # noqa: F401,E501


class Message(object):
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
        'owner': 'ChannelUsers',
        'text': 'str',
        'channel': 'str',
        'incident': 'str',
        'type': 'str',
        'edited': 'date',
        'last_thread_comment': 'date',
        'attachment': 'IncidentExternalIdMessageAttachment',
        'thread': 'list[MessageThreadComment]',
        'created': 'date',
        'modified': 'date',
        'organization': 'str',
        'tags': 'list[str]',
        'archived': 'bool'
    }

    attribute_map = {
        'id': '_id',
        'owner': 'owner',
        'text': 'text',
        'channel': 'channel',
        'incident': 'incident',
        'type': 'type',
        'edited': 'edited',
        'last_thread_comment': 'lastThreadComment',
        'attachment': 'attachment',
        'thread': 'thread',
        'created': 'created',
        'modified': 'modified',
        'organization': 'organization',
        'tags': 'tags',
        'archived': 'archived'
    }

    def __init__(self, id=None, owner=None, text=None, channel=None, incident=None, type=None, edited=None, last_thread_comment=None, attachment=None, thread=None, created=None, modified=None, organization=None, tags=None, archived=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._owner = None
        self._text = None
        self._channel = None
        self._incident = None
        self._type = None
        self._edited = None
        self._last_thread_comment = None
        self._attachment = None
        self._thread = None
        self._created = None
        self._modified = None
        self._organization = None
        self._tags = None
        self._archived = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        self.text = text
        if channel is not None:
            self.channel = channel
        if incident is not None:
            self.incident = incident
        self.type = type
        if edited is not None:
            self.edited = edited
        if last_thread_comment is not None:
            self.last_thread_comment = last_thread_comment
        if attachment is not None:
            self.attachment = attachment
        if thread is not None:
            self.thread = thread
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if organization is not None:
            self.organization = organization
        if tags is not None:
            self.tags = tags
        if archived is not None:
            self.archived = archived

    @property
    def id(self):
        """Gets the id of this Message.  # noqa: E501


        :return: The id of this Message.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Message.


        :param id: The id of this Message.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this Message.  # noqa: E501


        :return: The owner of this Message.  # noqa: E501
        :rtype: ChannelUsers
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Message.


        :param owner: The owner of this Message.  # noqa: E501
        :type: ChannelUsers
        """

        self._owner = owner

    @property
    def text(self):
        """Gets the text of this Message.  # noqa: E501


        :return: The text of this Message.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Message.


        :param text: The text of this Message.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def channel(self):
        """Gets the channel of this Message.  # noqa: E501

        Channel id to post to the channel  # noqa: E501

        :return: The channel of this Message.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this Message.

        Channel id to post to the channel  # noqa: E501

        :param channel: The channel of this Message.  # noqa: E501
        :type: str
        """

        self._channel = channel

    @property
    def incident(self):
        """Gets the incident of this Message.  # noqa: E501

        Incident id to post to the incident  # noqa: E501

        :return: The incident of this Message.  # noqa: E501
        :rtype: str
        """
        return self._incident

    @incident.setter
    def incident(self, incident):
        """Sets the incident of this Message.

        Incident id to post to the incident  # noqa: E501

        :param incident: The incident of this Message.  # noqa: E501
        :type: str
        """

        self._incident = incident

    @property
    def type(self):
        """Gets the type of this Message.  # noqa: E501


        :return: The type of this Message.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Message.


        :param type: The type of this Message.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["manualPost", "image", "file", "audit"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def edited(self):
        """Gets the edited of this Message.  # noqa: E501


        :return: The edited of this Message.  # noqa: E501
        :rtype: date
        """
        return self._edited

    @edited.setter
    def edited(self, edited):
        """Sets the edited of this Message.


        :param edited: The edited of this Message.  # noqa: E501
        :type: date
        """

        self._edited = edited

    @property
    def last_thread_comment(self):
        """Gets the last_thread_comment of this Message.  # noqa: E501

        Last read date of any of thread comments  # noqa: E501

        :return: The last_thread_comment of this Message.  # noqa: E501
        :rtype: date
        """
        return self._last_thread_comment

    @last_thread_comment.setter
    def last_thread_comment(self, last_thread_comment):
        """Sets the last_thread_comment of this Message.

        Last read date of any of thread comments  # noqa: E501

        :param last_thread_comment: The last_thread_comment of this Message.  # noqa: E501
        :type: date
        """

        self._last_thread_comment = last_thread_comment

    @property
    def attachment(self):
        """Gets the attachment of this Message.  # noqa: E501


        :return: The attachment of this Message.  # noqa: E501
        :rtype: IncidentExternalIdMessageAttachment
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this Message.


        :param attachment: The attachment of this Message.  # noqa: E501
        :type: IncidentExternalIdMessageAttachment
        """

        self._attachment = attachment

    @property
    def thread(self):
        """Gets the thread of this Message.  # noqa: E501


        :return: The thread of this Message.  # noqa: E501
        :rtype: list[MessageThreadComment]
        """
        return self._thread

    @thread.setter
    def thread(self, thread):
        """Sets the thread of this Message.


        :param thread: The thread of this Message.  # noqa: E501
        :type: list[MessageThreadComment]
        """

        self._thread = thread

    @property
    def created(self):
        """Gets the created of this Message.  # noqa: E501


        :return: The created of this Message.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Message.


        :param created: The created of this Message.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Message.  # noqa: E501


        :return: The modified of this Message.  # noqa: E501
        :rtype: date
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Message.


        :param modified: The modified of this Message.  # noqa: E501
        :type: date
        """

        self._modified = modified

    @property
    def organization(self):
        """Gets the organization of this Message.  # noqa: E501

        Organization id  # noqa: E501

        :return: The organization of this Message.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Message.

        Organization id  # noqa: E501

        :param organization: The organization of this Message.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def tags(self):
        """Gets the tags of this Message.  # noqa: E501


        :return: The tags of this Message.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Message.


        :param tags: The tags of this Message.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def archived(self):
        """Gets the archived of this Message.  # noqa: E501


        :return: The archived of this Message.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Message.


        :param archived: The archived of this Message.  # noqa: E501
        :type: bool
        """

        self._archived = archived

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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
