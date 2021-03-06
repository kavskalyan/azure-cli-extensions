# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._healthcare_apis_management_client_enums import *


class CheckNameAvailabilityParameters(msrest.serialization.Model):
    """Input values.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the service instance to check.
    :type name: str
    :param type: Required. The fully qualified resource type which includes provider namespace.
    :type type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        type: str,
        **kwargs
    ):
        super(CheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = name
        self.type = type


class ErrorDetails(msrest.serialization.Model):
    """Error details.

    :param error: Object containing error details.
    :type error: ~healthcare_apis_management_client.models.ErrorDetailsInternal
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetailsInternal'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDetailsInternal"] = None,
        **kwargs
    ):
        super(ErrorDetails, self).__init__(**kwargs)
        self.error = error


class ErrorDetailsInternal(msrest.serialization.Model):
    """Error details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The target of the particular error.
    :vartype target: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetailsInternal, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None


class Operation(msrest.serialization.Model):
    """Service REST API operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Operation name: {provider}/{resource}/{read | write | action |
     delete}
    :vartype name: str
    :ivar origin: Default value is 'user,system'.
    :vartype origin: str
    :param display: The information displayed about the operation.
    :type display: ~azure.mgmt.healthcareapis.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
        'origin': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.origin = None
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: Service provider: Microsoft.HealthcareApis
    :vartype provider: str
    :ivar resource: Resource Type: Services
    :vartype resource: str
    :ivar operation: Name of the operation
    :vartype operation: str
    :ivar description: Friendly description for the operation,
    :vartype description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationListResult(msrest.serialization.Model):
    """A list of service operations. It contains a list of operations and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param next_link: The link used to get the next page of service description objects.
    :type next_link: str
    :ivar value: A list of service operations supported by the Microsoft.HealthcareApis resource
     provider.
    :vartype value: list[~healthcare_apis_management_client.models.Operation]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = None


class OperationResultsDescription(msrest.serialization.Model):
    """The properties indicating the operation result of an operation on a service.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the operation returned.
    :vartype id: str
    :ivar name: The name of the operation result.
    :vartype name: str
    :ivar status: The status of the operation being performed. Possible values
     include: 'Canceled', 'Succeeded', 'Failed', 'Requested', 'Running'
    :vartype status: str or
     ~azure.mgmt.healthcareapis.models.OperationResultStatus
    :ivar start_time: The time that the operation was started.
    :vartype start_time: str
    :param properties: Additional properties of the operation result.
    :type properties: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'status': {'readonly': True},
        'start_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        properties: Optional[object] = None,
        **kwargs
    ):
        super(OperationResultsDescription, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.status = None
        self.start_time = None
        self.properties = properties


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class PrivateEndpointConnection(Resource):
    """The Private Endpoint Connection resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar provisioning_state: The provisioning state of the private endpoint connection resource.
     Possible values include: "Succeeded", "Creating", "Deleting", "Failed".
    :vartype provisioning_state: str or
     ~healthcare_apis_management_client.models.PrivateEndpointConnectionProvisioningState
    :param status: Indicates whether the connection has been Approved/Rejected/Removed by the owner
     of the service. Possible values include: "Pending", "Approved", "Rejected".
    :type status: str or
     ~healthcare_apis_management_client.models.PrivateEndpointServiceConnectionStatus
    :param description: The reason for approval/rejection of the connection.
    :type description: str
    :param actions_required: A message indicating if changes on the service provider require any
     updates on the consumer.
    :type actions_required: str
    :ivar id_private_endpoint_id: The ARM identifier for Private Endpoint.
    :vartype id_private_endpoint_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'id_private_endpoint_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'status': {'key': 'privateLinkServiceConnectionState.status', 'type': 'str'},
        'description': {'key': 'privateLinkServiceConnectionState.description', 'type': 'str'},
        'actions_required': {'key': 'privateLinkServiceConnectionState.actionsRequired', 'type': 'str'},
        'id_private_endpoint_id': {'key': 'privateEndpoint.id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        status: Optional[Union[str, "PrivateEndpointServiceConnectionStatus"]] = None,
        description: Optional[str] = None,
        actions_required: Optional[str] = None,
        **kwargs
    ):
        super(PrivateEndpointConnection, self).__init__(**kwargs)
        self.provisioning_state = None
        self.status = status
        self.description = description
        self.actions_required = actions_required
        self.id_private_endpoint_id = None


class PrivateEndpointConnectionListResult(msrest.serialization.Model):
    """List of private endpoint connection associated with the specified storage account.

    :param value: Array of private endpoint connections.
    :type value: list[~healthcare_apis_management_client.models.PrivateEndpointConnection]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PrivateEndpointConnection]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PrivateEndpointConnection"]] = None,
        **kwargs
    ):
        super(PrivateEndpointConnectionListResult, self).__init__(**kwargs)
        self.value = value


class PrivateLinkResource(Resource):
    """A private link resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar group_id: The private link resource group id.
    :vartype group_id: str
    :ivar required_members: The private link resource required member names.
    :vartype required_members: list[str]
    :param required_zone_names: The private link resource Private link DNS zone name.
    :type required_zone_names: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'group_id': {'readonly': True},
        'required_members': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'group_id': {'key': 'properties.groupId', 'type': 'str'},
        'required_members': {'key': 'properties.requiredMembers', 'type': '[str]'},
        'required_zone_names': {'key': 'properties.requiredZoneNames', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        required_zone_names: Optional[List[str]] = None,
        **kwargs
    ):
        super(PrivateLinkResource, self).__init__(**kwargs)
        self.group_id = None
        self.required_members = None
        self.required_zone_names = required_zone_names


class PrivateLinkResourceListResult(msrest.serialization.Model):
    """A list of private link resources.

    :param value: Array of private link resources.
    :type value: list[~healthcare_apis_management_client.models.PrivateLinkResource]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PrivateLinkResource]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PrivateLinkResource"]] = None,
        **kwargs
    ):
        super(PrivateLinkResourceListResult, self).__init__(**kwargs)
        self.value = value


class ServiceAccessPolicyEntry(msrest.serialization.Model):
    """An access policy entry.

    All required parameters must be populated in order to send to Azure.

    :param object_id: Required. An Azure AD object ID (User or Apps) that is allowed access to the
     FHIR service.
    :type object_id: str
    """

    _validation = {
        'object_id': {'required': True, 'pattern': r'^(([0-9A-Fa-f]{8}[-]?(?:[0-9A-Fa-f]{4}[-]?){3}[0-9A-Fa-f]{12}){1})+$'},
    }

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        object_id: str,
        **kwargs
    ):
        super(ServiceAccessPolicyEntry, self).__init__(**kwargs)
        self.object_id = object_id


class ServiceAuthenticationConfigurationInfo(msrest.serialization.Model):
    """Authentication configuration information.

    :param authority: The authority url for the service.
    :type authority: str
    :param audience: The audience url for the service.
    :type audience: str
    :param smart_proxy_enabled: If the SMART on FHIR proxy is enabled.
    :type smart_proxy_enabled: bool
    """

    _attribute_map = {
        'authority': {'key': 'authority', 'type': 'str'},
        'audience': {'key': 'audience', 'type': 'str'},
        'smart_proxy_enabled': {'key': 'smartProxyEnabled', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        authority: Optional[str] = None,
        audience: Optional[str] = None,
        smart_proxy_enabled: Optional[bool] = None,
        **kwargs
    ):
        super(ServiceAuthenticationConfigurationInfo, self).__init__(**kwargs)
        self.authority = authority
        self.audience = audience
        self.smart_proxy_enabled = smart_proxy_enabled


class ServiceCorsConfigurationInfo(msrest.serialization.Model):
    """The settings for the CORS configuration of the service instance.

    :param origins: The origins to be allowed via CORS.
    :type origins: list[str]
    :param headers: The headers to be allowed via CORS.
    :type headers: list[str]
    :param methods: The methods to be allowed via CORS.
    :type methods: list[str]
    :param max_age: The max age to be allowed via CORS.
    :type max_age: int
    :param allow_credentials: If credentials are allowed via CORS.
    :type allow_credentials: bool
    """

    _validation = {
        'max_age': {'maximum': 99999, 'minimum': 0},
    }

    _attribute_map = {
        'origins': {'key': 'origins', 'type': '[str]'},
        'headers': {'key': 'headers', 'type': '[str]'},
        'methods': {'key': 'methods', 'type': '[str]'},
        'max_age': {'key': 'maxAge', 'type': 'int'},
        'allow_credentials': {'key': 'allowCredentials', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        origins: Optional[List[str]] = None,
        headers: Optional[List[str]] = None,
        methods: Optional[List[str]] = None,
        max_age: Optional[int] = None,
        allow_credentials: Optional[bool] = None,
        **kwargs
    ):
        super(ServiceCorsConfigurationInfo, self).__init__(**kwargs)
        self.origins = origins
        self.headers = headers
        self.methods = methods
        self.max_age = max_age
        self.allow_credentials = allow_credentials


class ServiceCosmosDbConfigurationInfo(msrest.serialization.Model):
    """The settings for the Cosmos DB database backing the service.

    :param offer_throughput: The provisioned throughput for the backing
     database.
    :type offer_throughput: int
    :param key_vault_key_uri: The URI of the customer-managed key for the
     backing database.
    :type key_vault_key_uri: str
    """

    _validation = {
        'offer_throughput': {'maximum': 10000, 'minimum': 400},
    }

    _attribute_map = {
        'offer_throughput': {'key': 'offerThroughput', 'type': 'int'},
        'key_vault_key_uri': {'key': 'keyVaultKeyUri', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        offer_throughput: Optional[int] = None,
        key_vault_key_uri: Optional[str] = None,
        **kwargs
    ):
        super(ServiceCosmosDbConfigurationInfo, self).__init__(**kwargs)
        self.offer_throughput = offer_throughput
        self.key_vault_key_uri = key_vault_key_uri


class ServiceExportConfigurationInfo(msrest.serialization.Model):
    """Export operation configuration information.

    :param storage_account_name: The name of the default export storage
     account.
    :type storage_account_name: str
    """

    _attribute_map = {
        'storage_account_name': {'key': 'storageAccountName', 'type': 'str'},
    }

    def __init__(self, *, storage_account_name: str=None, **kwargs) -> None:
        super(ServiceExportConfigurationInfo, self).__init__(**kwargs)
        self.storage_account_name = storage_account_name


class ServicesResource(msrest.serialization.Model):
    """The common properties of a service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param kind: Required. The kind of the service. Possible values include:
     'fhir', 'fhir-Stu3', 'fhir-R4'
    :type kind: str or ~azure.mgmt.healthcareapis.models.Kind
    :param location: Required. The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param etag: An etag associated with the resource, used for optimistic concurrency when editing
     it.
    :type etag: str
    :ivar principal_id: The principal ID of the resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the resource.
    :vartype tenant_id: str
    :param type_identity_type: Type of identity being specified, currently SystemAssigned and None
     are allowed. Possible values include: "SystemAssigned", "None".
    :type type_identity_type: str or
     ~healthcare_apis_management_client.models.ManagedServiceIdentityType
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^[a-z0-9][a-z0-9-]{1,21}[a-z0-9]$'},
        'type': {'readonly': True},
        'kind': {'required': True},
        'location': {'required': True},
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'principal_id': {'key': 'identity.principalId', 'type': 'str'},
        'tenant_id': {'key': 'identity.tenantId', 'type': 'str'},
        'type_identity_type': {'key': 'identity.type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        kind: Union[str, "Kind"],
        location: str,
        tags: Optional[Dict[str, str]] = None,
        etag: Optional[str] = None,
        type_identity_type: Optional[Union[str, "ManagedServiceIdentityType"]] = None,
        **kwargs
    ):
        super(ServicesResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.kind = kind
        self.location = location
        self.tags = tags
        self.etag = etag
        self.principal_id = None
        self.tenant_id = None
        self.type_identity_type = type_identity_type


class ServicesDescription(ServicesResource):
    """The description of the service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param kind: Required. The kind of the service. Possible values include:
     'fhir', 'fhir-Stu3', 'fhir-R4'
    :type kind: str or ~healthcare_apis_management_client.models.Kind
    :param location: Required. The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param etag: An etag associated with the resource, used for optimistic concurrency when editing
     it.
    :type etag: str
    :ivar principal_id: The principal ID of the resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the resource.
    :vartype tenant_id: str
    :param type_identity_type: Type of identity being specified, currently SystemAssigned and None
     are allowed. Possible values include: "SystemAssigned", "None".
    :type type_identity_type: str or
     ~healthcare_apis_management_client.models.ManagedServiceIdentityType
    :ivar provisioning_state: The provisioning state. Possible values include: "Deleting",
     "Succeeded", "Creating", "Accepted", "Verifying", "Updating", "Failed", "Canceled",
     "Deprovisioned".
    :vartype provisioning_state: str or ~healthcare_apis_management_client.models.ProvisioningState
    :param access_policies: The access policies of the service instance.
    :type access_policies: list[~healthcare_apis_management_client.models.ServiceAccessPolicyEntry]
    :param cosmos_db_configuration: The settings for the Cosmos DB database backing the service.
    :type cosmos_db_configuration:
     ~healthcare_apis_management_client.models.ServiceCosmosDBConfigurationInfo
    :param authentication_configuration: The authentication configuration for the service instance.
    :type authentication_configuration:
     ~healthcare_apis_management_client.models.ServiceAuthenticationConfigurationInfo
    :param cors_configuration: The settings for the CORS configuration of the service instance.
    :type cors_configuration:
     ~healthcare_apis_management_client.models.ServiceCorsConfigurationInfo
    :param private_endpoint_connections: The list of private endpoint connections that are set up
     for this resource.
    :type private_endpoint_connections:
     list[~healthcare_apis_management_client.models.PrivateEndpointConnection]
    :param public_network_access: Control permission for data plane traffic coming from public
     networks while private endpoint is enabled. Possible values include: "Enabled", "Disabled".
    :type public_network_access: str or
     ~healthcare_apis_management_client.models.PublicNetworkAccess
    :param storage_account_name: The name of the default export storage account.
    :type storage_account_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^[a-z0-9][a-z0-9-]{1,21}[a-z0-9]$'},
        'type': {'readonly': True},
        'kind': {'required': True},
        'location': {'required': True},
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'principal_id': {'key': 'identity.principalId', 'type': 'str'},
        'tenant_id': {'key': 'identity.tenantId', 'type': 'str'},
        'type_identity_type': {'key': 'identity.type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'access_policies': {'key': 'properties.accessPolicies', 'type': '[ServiceAccessPolicyEntry]'},
        'cosmos_db_configuration': {'key': 'properties.cosmosDbConfiguration', 'type': 'ServiceCosmosDBConfigurationInfo'},
        'authentication_configuration': {'key': 'properties.authenticationConfiguration', 'type': 'ServiceAuthenticationConfigurationInfo'},
        'cors_configuration': {'key': 'properties.corsConfiguration', 'type': 'ServiceCorsConfigurationInfo'},
        'private_endpoint_connections': {'key': 'properties.privateEndpointConnections', 'type': '[PrivateEndpointConnection]'},
        'public_network_access': {'key': 'properties.publicNetworkAccess', 'type': 'str'},
        'storage_account_name': {'key': 'properties.exportConfiguration.storageAccountName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        kind: Union[str, "Kind"],
        location: str,
        tags: Optional[Dict[str, str]] = None,
        etag: Optional[str] = None,
        type_identity_type: Optional[Union[str, "ManagedServiceIdentityType"]] = None,
        access_policies: Optional[List["ServiceAccessPolicyEntry"]] = None,
        cosmos_db_configuration: Optional["ServiceCosmosDBConfigurationInfo"] = None,
        authentication_configuration: Optional["ServiceAuthenticationConfigurationInfo"] = None,
        cors_configuration: Optional["ServiceCorsConfigurationInfo"] = None,
        private_endpoint_connections: Optional[List["PrivateEndpointConnection"]] = None,
        public_network_access: Optional[Union[str, "PublicNetworkAccess"]] = None,
        storage_account_name: Optional[str] = None,
        **kwargs
    ):
        super(ServicesDescription, self).__init__(kind=kind, location=location, tags=tags, etag=etag, type_identity_type=type_identity_type, **kwargs)
        self.provisioning_state = None
        self.access_policies = access_policies
        self.cosmos_db_configuration = cosmos_db_configuration
        self.authentication_configuration = authentication_configuration
        self.cors_configuration = cors_configuration
        self.private_endpoint_connections = private_endpoint_connections
        self.public_network_access = public_network_access
        self.storage_account_name = storage_account_name


class ServicesDescriptionListResult(msrest.serialization.Model):
    """A list of service description objects with a next link.

    :param next_link: The link used to get the next page of service description objects.
    :type next_link: str
    :param value: A list of service description objects.
    :type value: list[~healthcare_apis_management_client.models.ServicesDescription]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[ServicesDescription]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        value: Optional[List["ServicesDescription"]] = None,
        **kwargs
    ):
        super(ServicesDescriptionListResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class ServicesNameAvailabilityInfo(msrest.serialization.Model):
    """The properties indicating whether a given service name is available.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name_available: The value which indicates whether the provided name
     is available.
    :vartype name_available: bool
    :ivar reason: The reason for unavailability. Possible values include:
     'Invalid', 'AlreadyExists'
    :vartype reason: str or
     ~healthcare_apis_management_client.models.ServiceNameUnavailabilityReason
    :param message: The detailed reason message.
    :type message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ServicesNameAvailabilityInfo, self).__init__(**kwargs)
        self.name_available = None
        self.reason = None
        self.message = message


class ServicesPatchDescription(msrest.serialization.Model):
    """The description of the service.

    :param tags: A set of tags. Instance tags.
    :type tags: dict[str, str]
    :param public_network_access: Control permission for data plane traffic coming from public
     coming from public networks while private endpoint is enabled. Possible
     values include: 'Enabled', 'Disabled'
    :type public_network_access: str or
     ~healthcare_apis_management_client.models.PublicNetworkAccess
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'public_network_access': {'key': 'properties.publicNetworkAccess', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        public_network_access: Optional[Union[str, "PublicNetworkAccess"]] = None,
        **kwargs
    ):
        super(ServicesPatchDescription, self).__init__(**kwargs)
        self.tags = tags
        self.public_network_access = public_network_access
