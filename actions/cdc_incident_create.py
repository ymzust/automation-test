import cdc.sdk
import json
import os
from st2common.runners.base_action import Action

class IncidentCreate(Action):
    def run(self, incident_name, incident_description, incident_priority, incident_severity, incident_source, incident_type):
        organization = 
        incident = new_incident = cdc.model.Incident(
            name=name,
            description=description,
            organization=os.getenv('CDC_ORGANIZATION_KEY'),
            priority= priority,
            severity=severity,
            status="New",
            source=source,
            type=type,
            tags=[],
            playbooks=[]
        )
        return cdc.sdk.incident.create_incident(incident)