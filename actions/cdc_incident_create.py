import cdc
import os
from st2common.runners.base_action import Action

class IncidentCreate(Action):
    def run(self, incident_name, incident_description, incident_priority, incident_severity, incident_source, incident_type):
        incident = cdc.model.Incident(
            name=incident_name,
            description=incident_description,
            organization=cdc.settings().organization,
            priority=incident_priority,
            severity=incident_severity,
            status="New",
            source=incident_source,
            type=incident_type,
            tags=[],
            playbooks=[]
        )
        return cdc.incident.create_incident(incident)