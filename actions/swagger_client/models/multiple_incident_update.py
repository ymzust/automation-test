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
from swagger_client.models.cpp_alert_edges import CppAlertEdges  # noqa: F401,E501
from swagger_client.models.incident_evidence import IncidentEvidence  # noqa: F401,E501
from swagger_client.models.incident_external import IncidentExternal  # noqa: F401,E501
from swagger_client.models.incident_organization import IncidentOrganization  # noqa: F401,E501
from swagger_client.models.incident_related_incidents import IncidentRelatedIncidents  # noqa: F401,E501
from swagger_client.models.incident_summary import IncidentSummary  # noqa: F401,E501
from swagger_client.models.observable import Observable  # noqa: F401,E501
from swagger_client.models.observable_owner import ObservableOwner  # noqa: F401,E501
from swagger_client.models.raw_alert import RawAlert  # noqa: F401,E501


class MultipleIncidentUpdate(object):
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
        'alerts': 'list[RawAlert]',
        'created': 'date',
        'created_by': 'ChannelUsers',
        'closed': 'date',
        'description': 'str',
        'edges': 'list[CppAlertEdges]',
        'evidences': 'list[IncidentEvidence]',
        'external': 'list[IncidentExternal]',
        'key': 'str',
        'last_read': 'date',
        'last_read_thread': 'date',
        'modified': 'date',
        'name': 'str',
        'number_of_alerts': 'float',
        'number_of_events': 'float',
        'number_of_observables': 'float',
        'observables': 'list[Observable]',
        'organization': 'IncidentOrganization',
        'owner': 'ObservableOwner',
        'playbooks': 'list[object]',
        'priority': 'str',
        'read_only': 'bool',
        'related_incidents': 'IncidentRelatedIncidents',
        'root': 'str',
        'severity': 'str',
        'status': 'str',
        'source': 'str',
        'summary': 'IncidentSummary',
        'tags': 'list[str]',
        'total_open_time': 'float',
        'type': 'str',
        'unread': 'bool',
        'eid': 'list[str]'
    }

    attribute_map = {
        'id': '_id',
        'alerts': 'alerts',
        'created': 'created',
        'created_by': 'createdBy',
        'closed': 'closed',
        'description': 'description',
        'edges': 'edges',
        'evidences': 'evidences',
        'external': 'external',
        'key': 'key',
        'last_read': 'lastRead',
        'last_read_thread': 'lastReadThread',
        'modified': 'modified',
        'name': 'name',
        'number_of_alerts': 'numberOfAlerts',
        'number_of_events': 'numberOfEvents',
        'number_of_observables': 'numberOfObservables',
        'observables': 'observables',
        'organization': 'organization',
        'owner': 'owner',
        'playbooks': 'playbooks',
        'priority': 'priority',
        'read_only': 'readOnly',
        'related_incidents': 'relatedIncidents',
        'root': 'root',
        'severity': 'severity',
        'status': 'status',
        'source': 'source',
        'summary': 'summary',
        'tags': 'tags',
        'total_open_time': 'totalOpenTime',
        'type': 'type',
        'unread': 'unread',
        'eid': 'id'
    }

    def __init__(self, id=None, alerts=None, created=None, created_by=None, closed=None, description=None, edges=None, evidences=None, external=None, key=None, last_read=None, last_read_thread=None, modified=None, name=None, number_of_alerts=None, number_of_events=None, number_of_observables=None, observables=None, organization=None, owner=None, playbooks=None, priority=None, read_only=None, related_incidents=None, root=None, severity=None, status=None, source=None, summary=None, tags=None, total_open_time=None, type=None, unread=None, eid=None):  # noqa: E501
        """MultipleIncidentUpdate - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._alerts = None
        self._created = None
        self._created_by = None
        self._closed = None
        self._description = None
        self._edges = None
        self._evidences = None
        self._external = None
        self._key = None
        self._last_read = None
        self._last_read_thread = None
        self._modified = None
        self._name = None
        self._number_of_alerts = None
        self._number_of_events = None
        self._number_of_observables = None
        self._observables = None
        self._organization = None
        self._owner = None
        self._playbooks = None
        self._priority = None
        self._read_only = None
        self._related_incidents = None
        self._root = None
        self._severity = None
        self._status = None
        self._source = None
        self._summary = None
        self._tags = None
        self._total_open_time = None
        self._type = None
        self._unread = None
        self._eid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if alerts is not None:
            self.alerts = alerts
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if closed is not None:
            self.closed = closed
        self.description = description
        if edges is not None:
            self.edges = edges
        if evidences is not None:
            self.evidences = evidences
        if external is not None:
            self.external = external
        if key is not None:
            self.key = key
        if last_read is not None:
            self.last_read = last_read
        if last_read_thread is not None:
            self.last_read_thread = last_read_thread
        if modified is not None:
            self.modified = modified
        self.name = name
        if number_of_alerts is not None:
            self.number_of_alerts = number_of_alerts
        if number_of_events is not None:
            self.number_of_events = number_of_events
        if number_of_observables is not None:
            self.number_of_observables = number_of_observables
        if observables is not None:
            self.observables = observables
        self.organization = organization
        if owner is not None:
            self.owner = owner
        if playbooks is not None:
            self.playbooks = playbooks
        self.priority = priority
        if read_only is not None:
            self.read_only = read_only
        if related_incidents is not None:
            self.related_incidents = related_incidents
        if root is not None:
            self.root = root
        self.severity = severity
        self.status = status
        if source is not None:
            self.source = source
        if summary is not None:
            self.summary = summary
        if tags is not None:
            self.tags = tags
        if total_open_time is not None:
            self.total_open_time = total_open_time
        self.type = type
        if unread is not None:
            self.unread = unread
        if eid is not None:
            self.eid = eid

    @property
    def id(self):
        """Gets the id of this MultipleIncidentUpdate.  # noqa: E501

        Incident id (database)  # noqa: E501

        :return: The id of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MultipleIncidentUpdate.

        Incident id (database)  # noqa: E501

        :param id: The id of this MultipleIncidentUpdate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def alerts(self):
        """Gets the alerts of this MultipleIncidentUpdate.  # noqa: E501


        :return: The alerts of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: list[RawAlert]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this MultipleIncidentUpdate.


        :param alerts: The alerts of this MultipleIncidentUpdate.  # noqa: E501
        :type: list[RawAlert]
        """

        self._alerts = alerts

    @property
    def created(self):
        """Gets the created of this MultipleIncidentUpdate.  # noqa: E501


        :return: The created of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MultipleIncidentUpdate.


        :param created: The created of this MultipleIncidentUpdate.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this MultipleIncidentUpdate.  # noqa: E501


        :return: The created_by of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: ChannelUsers
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this MultipleIncidentUpdate.


        :param created_by: The created_by of this MultipleIncidentUpdate.  # noqa: E501
        :type: ChannelUsers
        """

        self._created_by = created_by

    @property
    def closed(self):
        """Gets the closed of this MultipleIncidentUpdate.  # noqa: E501

        Incident closed date  # noqa: E501

        :return: The closed of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: date
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this MultipleIncidentUpdate.

        Incident closed date  # noqa: E501

        :param closed: The closed of this MultipleIncidentUpdate.  # noqa: E501
        :type: date
        """

        self._closed = closed

    @property
    def description(self):
        """Gets the description of this MultipleIncidentUpdate.  # noqa: E501


        :return: The description of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MultipleIncidentUpdate.


        :param description: The description of this MultipleIncidentUpdate.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def edges(self):
        """Gets the edges of this MultipleIncidentUpdate.  # noqa: E501


        :return: The edges of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: list[CppAlertEdges]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this MultipleIncidentUpdate.


        :param edges: The edges of this MultipleIncidentUpdate.  # noqa: E501
        :type: list[CppAlertEdges]
        """

        self._edges = edges

    @property
    def evidences(self):
        """Gets the evidences of this MultipleIncidentUpdate.  # noqa: E501


        :return: The evidences of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: list[IncidentEvidence]
        """
        return self._evidences

    @evidences.setter
    def evidences(self, evidences):
        """Sets the evidences of this MultipleIncidentUpdate.


        :param evidences: The evidences of this MultipleIncidentUpdate.  # noqa: E501
        :type: list[IncidentEvidence]
        """

        self._evidences = evidences

    @property
    def external(self):
        """Gets the external of this MultipleIncidentUpdate.  # noqa: E501


        :return: The external of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: list[IncidentExternal]
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this MultipleIncidentUpdate.


        :param external: The external of this MultipleIncidentUpdate.  # noqa: E501
        :type: list[IncidentExternal]
        """

        self._external = external

    @property
    def key(self):
        """Gets the key of this MultipleIncidentUpdate.  # noqa: E501

        Incident id (human-readable)  # noqa: E501

        :return: The key of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MultipleIncidentUpdate.

        Incident id (human-readable)  # noqa: E501

        :param key: The key of this MultipleIncidentUpdate.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def last_read(self):
        """Gets the last_read of this MultipleIncidentUpdate.  # noqa: E501

        When current user last accessed incident  # noqa: E501

        :return: The last_read of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: date
        """
        return self._last_read

    @last_read.setter
    def last_read(self, last_read):
        """Sets the last_read of this MultipleIncidentUpdate.

        When current user last accessed incident  # noqa: E501

        :param last_read: The last_read of this MultipleIncidentUpdate.  # noqa: E501
        :type: date
        """

        self._last_read = last_read

    @property
    def last_read_thread(self):
        """Gets the last_read_thread of this MultipleIncidentUpdate.  # noqa: E501

        When any of wall threads was accessed  # noqa: E501

        :return: The last_read_thread of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: date
        """
        return self._last_read_thread

    @last_read_thread.setter
    def last_read_thread(self, last_read_thread):
        """Sets the last_read_thread of this MultipleIncidentUpdate.

        When any of wall threads was accessed  # noqa: E501

        :param last_read_thread: The last_read_thread of this MultipleIncidentUpdate.  # noqa: E501
        :type: date
        """

        self._last_read_thread = last_read_thread

    @property
    def modified(self):
        """Gets the modified of this MultipleIncidentUpdate.  # noqa: E501


        :return: The modified of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: date
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this MultipleIncidentUpdate.


        :param modified: The modified of this MultipleIncidentUpdate.  # noqa: E501
        :type: date
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this MultipleIncidentUpdate.  # noqa: E501


        :return: The name of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MultipleIncidentUpdate.


        :param name: The name of this MultipleIncidentUpdate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def number_of_alerts(self):
        """Gets the number_of_alerts of this MultipleIncidentUpdate.  # noqa: E501


        :return: The number_of_alerts of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: float
        """
        return self._number_of_alerts

    @number_of_alerts.setter
    def number_of_alerts(self, number_of_alerts):
        """Sets the number_of_alerts of this MultipleIncidentUpdate.


        :param number_of_alerts: The number_of_alerts of this MultipleIncidentUpdate.  # noqa: E501
        :type: float
        """

        self._number_of_alerts = number_of_alerts

    @property
    def number_of_events(self):
        """Gets the number_of_events of this MultipleIncidentUpdate.  # noqa: E501


        :return: The number_of_events of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: float
        """
        return self._number_of_events

    @number_of_events.setter
    def number_of_events(self, number_of_events):
        """Sets the number_of_events of this MultipleIncidentUpdate.


        :param number_of_events: The number_of_events of this MultipleIncidentUpdate.  # noqa: E501
        :type: float
        """

        self._number_of_events = number_of_events

    @property
    def number_of_observables(self):
        """Gets the number_of_observables of this MultipleIncidentUpdate.  # noqa: E501


        :return: The number_of_observables of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: float
        """
        return self._number_of_observables

    @number_of_observables.setter
    def number_of_observables(self, number_of_observables):
        """Sets the number_of_observables of this MultipleIncidentUpdate.


        :param number_of_observables: The number_of_observables of this MultipleIncidentUpdate.  # noqa: E501
        :type: float
        """

        self._number_of_observables = number_of_observables

    @property
    def observables(self):
        """Gets the observables of this MultipleIncidentUpdate.  # noqa: E501


        :return: The observables of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: list[Observable]
        """
        return self._observables

    @observables.setter
    def observables(self, observables):
        """Sets the observables of this MultipleIncidentUpdate.


        :param observables: The observables of this MultipleIncidentUpdate.  # noqa: E501
        :type: list[Observable]
        """

        self._observables = observables

    @property
    def organization(self):
        """Gets the organization of this MultipleIncidentUpdate.  # noqa: E501


        :return: The organization of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: IncidentOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this MultipleIncidentUpdate.


        :param organization: The organization of this MultipleIncidentUpdate.  # noqa: E501
        :type: IncidentOrganization
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def owner(self):
        """Gets the owner of this MultipleIncidentUpdate.  # noqa: E501


        :return: The owner of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: ObservableOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this MultipleIncidentUpdate.


        :param owner: The owner of this MultipleIncidentUpdate.  # noqa: E501
        :type: ObservableOwner
        """

        self._owner = owner

    @property
    def playbooks(self):
        """Gets the playbooks of this MultipleIncidentUpdate.  # noqa: E501


        :return: The playbooks of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: list[object]
        """
        return self._playbooks

    @playbooks.setter
    def playbooks(self, playbooks):
        """Sets the playbooks of this MultipleIncidentUpdate.


        :param playbooks: The playbooks of this MultipleIncidentUpdate.  # noqa: E501
        :type: list[object]
        """

        self._playbooks = playbooks

    @property
    def priority(self):
        """Gets the priority of this MultipleIncidentUpdate.  # noqa: E501

        Value is taken from metamodels  # noqa: E501

        :return: The priority of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this MultipleIncidentUpdate.

        Value is taken from metamodels  # noqa: E501

        :param priority: The priority of this MultipleIncidentUpdate.  # noqa: E501
        :type: str
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501
        allowed_values = ["Low", "Medium", "High"]  # noqa: E501
        if priority not in allowed_values:
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

    @property
    def read_only(self):
        """Gets the read_only of this MultipleIncidentUpdate.  # noqa: E501


        :return: The read_only of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this MultipleIncidentUpdate.


        :param read_only: The read_only of this MultipleIncidentUpdate.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def related_incidents(self):
        """Gets the related_incidents of this MultipleIncidentUpdate.  # noqa: E501


        :return: The related_incidents of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: IncidentRelatedIncidents
        """
        return self._related_incidents

    @related_incidents.setter
    def related_incidents(self, related_incidents):
        """Sets the related_incidents of this MultipleIncidentUpdate.


        :param related_incidents: The related_incidents of this MultipleIncidentUpdate.  # noqa: E501
        :type: IncidentRelatedIncidents
        """

        self._related_incidents = related_incidents

    @property
    def root(self):
        """Gets the root of this MultipleIncidentUpdate.  # noqa: E501

        Root organization (top of the hierarchy)  # noqa: E501

        :return: The root of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this MultipleIncidentUpdate.

        Root organization (top of the hierarchy)  # noqa: E501

        :param root: The root of this MultipleIncidentUpdate.  # noqa: E501
        :type: str
        """

        self._root = root

    @property
    def severity(self):
        """Gets the severity of this MultipleIncidentUpdate.  # noqa: E501

        Value is taken from metamodels  # noqa: E501

        :return: The severity of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this MultipleIncidentUpdate.

        Value is taken from metamodels  # noqa: E501

        :param severity: The severity of this MultipleIncidentUpdate.  # noqa: E501
        :type: str
        """
        if severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501
        allowed_values = ["Low", "Medium", "High"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def status(self):
        """Gets the status of this MultipleIncidentUpdate.  # noqa: E501

        Values is taken from metamodels  # noqa: E501

        :return: The status of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MultipleIncidentUpdate.

        Values is taken from metamodels  # noqa: E501

        :param status: The status of this MultipleIncidentUpdate.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["New", "Open", "Pending", "Closed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def source(self):
        """Gets the source of this MultipleIncidentUpdate.  # noqa: E501

        How incident was created  # noqa: E501

        :return: The source of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this MultipleIncidentUpdate.

        How incident was created  # noqa: E501

        :param source: The source of this MultipleIncidentUpdate.  # noqa: E501
        :type: str
        """
        allowed_values = ["manual", "alerts"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def summary(self):
        """Gets the summary of this MultipleIncidentUpdate.  # noqa: E501


        :return: The summary of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: IncidentSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this MultipleIncidentUpdate.


        :param summary: The summary of this MultipleIncidentUpdate.  # noqa: E501
        :type: IncidentSummary
        """

        self._summary = summary

    @property
    def tags(self):
        """Gets the tags of this MultipleIncidentUpdate.  # noqa: E501


        :return: The tags of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MultipleIncidentUpdate.


        :param tags: The tags of this MultipleIncidentUpdate.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def total_open_time(self):
        """Gets the total_open_time of this MultipleIncidentUpdate.  # noqa: E501

        How long incident was in status \"Open\" (ms)  # noqa: E501

        :return: The total_open_time of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: float
        """
        return self._total_open_time

    @total_open_time.setter
    def total_open_time(self, total_open_time):
        """Sets the total_open_time of this MultipleIncidentUpdate.

        How long incident was in status \"Open\" (ms)  # noqa: E501

        :param total_open_time: The total_open_time of this MultipleIncidentUpdate.  # noqa: E501
        :type: float
        """

        self._total_open_time = total_open_time

    @property
    def type(self):
        """Gets the type of this MultipleIncidentUpdate.  # noqa: E501

        Value is taken from metamodels. Below is default metamodels.  # noqa: E501

        :return: The type of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MultipleIncidentUpdate.

        Value is taken from metamodels. Below is default metamodels.  # noqa: E501

        :param type: The type of this MultipleIncidentUpdate.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Malware", "Ransomware", "DDOS", "Unauthorized access", "Insider breach", "Unauthorized previliged escalation", "Destructive attack", "Advanced persistent threat (APT)", "Other"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def unread(self):
        """Gets the unread of this MultipleIncidentUpdate.  # noqa: E501

        Is incident unread by current user  # noqa: E501

        :return: The unread of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._unread

    @unread.setter
    def unread(self, unread):
        """Sets the unread of this MultipleIncidentUpdate.

        Is incident unread by current user  # noqa: E501

        :param unread: The unread of this MultipleIncidentUpdate.  # noqa: E501
        :type: bool
        """

        self._unread = unread

    @property
    def eid(self):
        """Gets the eid of this MultipleIncidentUpdate.  # noqa: E501

        Incident ids to update  # noqa: E501

        :return: The eid of this MultipleIncidentUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._eid

    @eid.setter
    def eid(self, eid):
        """Sets the eid of this MultipleIncidentUpdate.

        Incident ids to update  # noqa: E501

        :param eid: The eid of this MultipleIncidentUpdate.  # noqa: E501
        :type: list[str]
        """

        self._eid = eid

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
        if not isinstance(other, MultipleIncidentUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
