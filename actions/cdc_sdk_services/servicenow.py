import sys
from SOAPpy import SOAPProxy

class ServiceNow(object):
    def __init__(self, instance, username, password):
        connection  = 'https://%s:%s@%s.service-now.com/incident.do?SOAP' %  (username, password, instance)
        self.service = SOAPProxy (connection , 'http://www.service-now.com/')

    def create_incident(params_dict):
        return self.service.insert(
            impact = int (params_dict [ 'impact' ] ) , 
            urgency = int (params_dict [ 'urgency' ] ) , 
            priority = int (params_dict [ 'priority' ] ) , 
            category =params_dict [ 'category' ] , 
            location =params_dict [ 'location' ] , 
            caller_id =params_dict [ 'user' ] , 
            assignment_group =params_dict [ 'assignment_group' ] , 
            assigned_to =params_dict [ 'assigned_to' ] , 
            short_description =params_dict [ 'short_description' ] , 
            comments =params_dict [ 'comments' ] 
        )