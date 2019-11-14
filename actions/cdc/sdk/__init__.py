from cdc.sdk.cdc_sdk_context import Context

from cdc.sdk.swagger_client.api_client import ApiClient
from cdc.sdk.swagger_client.configuration import Configuration

import cdc.sdk.swagger_client.api as backend
import cdc.sdk.swagger_client.models as backend_models

if (not Context.instance):
    Context.instance = Context()

alert = backend.AlertsApi(Context.instance.client)
channel = backend.ChannelsApi(Context.instance.client)
dashboard = backend.DashboardApi(Context.instance.client)
incident = backend.IncidentsApi(Context.instance.client)
message = backend.MessagesApi(Context.instance.client)
metamodel = backend.MetamodelsApi(Context.instance.client)
observable = backend.ObservablesApi(Context.instance.client)
organization = backend.OrganizationsApi(Context.instance.client)
playbook = backend.PlaybooksApi(Context.instance.client)
profile = backend.ProfileApi(Context.instance.client)
report = backend.ReportsApi(Context.instance.client)
search = backend.SearchApi(Context.instance.client)
survey = backend.SurveyApi(Context.instance.client)
tag = backend.TagsApi(Context.instance.client)
thread = backend.ThreadApi(Context.instance.client)
user = backend.UsersApi(Context.instance.client)
webhook = backend.WebhooksApi(Context.instance.client)

model = backend_models