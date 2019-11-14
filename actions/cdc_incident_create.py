import cdc.sdk
from st2common.runners.base_action import Action

class IncidentCreate(Action):
    def run(self, incident_body):
        return cdc.sdk.incident.create_incident(incident_body)