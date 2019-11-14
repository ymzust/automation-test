import cdc
import os
from st2common.runners.base_action import Action

class IncidentCreate(Action):
    def run(self, incident_name, incident_description, incident_priority, incident_severity, incident_source, incident_type):
        incident = cdc.model.Incident(
            name=name,
            description=description,
            organization=cdc.settings().organization,
            priority= priority,
            severity=severity,
            status="New",
            source=source,
            type=incident_type,
            tags=[],
            playbooks=[]
        )
        return incident.create_incident(incident)