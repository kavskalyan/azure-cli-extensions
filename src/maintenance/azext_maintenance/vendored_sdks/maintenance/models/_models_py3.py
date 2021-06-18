# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._maintenance_client_enums import *


class Resource(msrest.serialization.Model):
    """Definition of a Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified identifier of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~maintenance_client.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class ApplyUpdate(Resource):
    """Apply Update request.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified identifier of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~maintenance_client.models.SystemData
    :param status: The status. Possible values include: "Pending", "InProgress", "Completed",
     "RetryNow", "RetryLater".
    :type status: str or ~maintenance_client.models.UpdateStatus
    :param resource_id: The resourceId.
    :type resource_id: str
    :param last_update_time: Last Update time.
    :type last_update_time: ~datetime.datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
        'last_update_time': {'key': 'properties.lastUpdateTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        status: Optional[Union[str, "UpdateStatus"]] = None,
        resource_id: Optional[str] = None,
        last_update_time: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(ApplyUpdate, self).__init__(**kwargs)
        self.status = status
        self.resource_id = resource_id
        self.last_update_time = last_update_time


class ConfigurationAssignment(Resource):
    """Configuration Assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified identifier of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~maintenance_client.models.SystemData
    :param location: Location of the resource.
    :type location: str
    :param maintenance_configuration_id: The maintenance configuration Id.
    :type maintenance_configuration_id: str
    :param resource_id: The unique resourceId.
    :type resource_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'location': {'key': 'location', 'type': 'str'},
        'maintenance_configuration_id': {'key': 'properties.maintenanceConfigurationId', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        maintenance_configuration_id: Optional[str] = None,
        resource_id: Optional[str] = None,
        **kwargs
    ):
        super(ConfigurationAssignment, self).__init__(**kwargs)
        self.location = location
        self.maintenance_configuration_id = maintenance_configuration_id
        self.resource_id = resource_id


class ErrorDetails(msrest.serialization.Model):
    """An error response details received from the Azure Maintenance service.

    :param code: Service-defined error code. This code serves as a sub-status for the HTTP error
     code specified in the response.
    :type code: str
    :param message: Human-readable representation of the error.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorDetails, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ListApplyUpdate(msrest.serialization.Model):
    """Response for ApplyUpdate list.

    :param value: The list of apply updates.
    :type value: list[~maintenance_client.models.ApplyUpdate]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ApplyUpdate]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ApplyUpdate"]] = None,
        **kwargs
    ):
        super(ListApplyUpdate, self).__init__(**kwargs)
        self.value = value


class ListConfigurationAssignmentsResult(msrest.serialization.Model):
    """Response for ConfigurationAssignments list.

    :param value: The list of configuration Assignments.
    :type value: list[~maintenance_client.models.ConfigurationAssignment]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ConfigurationAssignment]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ConfigurationAssignment"]] = None,
        **kwargs
    ):
        super(ListConfigurationAssignmentsResult, self).__init__(**kwargs)
        self.value = value


class ListMaintenanceConfigurationsResult(msrest.serialization.Model):
    """Response for MaintenanceConfigurations list.

    :param value: The list of maintenance Configurations.
    :type value: list[~maintenance_client.models.MaintenanceConfiguration]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MaintenanceConfiguration]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MaintenanceConfiguration"]] = None,
        **kwargs
    ):
        super(ListMaintenanceConfigurationsResult, self).__init__(**kwargs)
        self.value = value


class ListUpdatesResult(msrest.serialization.Model):
    """Response for Updates list.

    :param value: The pending updates.
    :type value: list[~maintenance_client.models.Update]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Update]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Update"]] = None,
        **kwargs
    ):
        super(ListUpdatesResult, self).__init__(**kwargs)
        self.value = value


class MaintenanceConfiguration(Resource):
    """Maintenance configuration record type.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified identifier of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~maintenance_client.models.SystemData
    :param location: Gets or sets location of the resource.
    :type location: str
    :param tags: A set of tags. Gets or sets tags of the resource.
    :type tags: dict[str, str]
    :param namespace: Gets or sets namespace of the resource.
    :type namespace: str
    :param extension_properties: Gets or sets extensionProperties of the maintenanceConfiguration.
    :type extension_properties: dict[str, str]
    :param maintenance_scope: Gets or sets maintenanceScope of the configuration. Possible values
     include: "Host", "OSImage", "Extension", "InGuestPatch", "SQLDB", "SQLManagedInstance".
    :type maintenance_scope: str or ~maintenance_client.models.MaintenanceScope
    :param visibility: Gets or sets the visibility of the configuration. The default value is
     'Custom'. Possible values include: "Custom", "Public".
    :type visibility: str or ~maintenance_client.models.Visibility
    :param start_date_time: Effective start date of the maintenance window in YYYY-MM-DD hh:mm
     format. The start date can be set to either the current date or future date. The window will be
     created in the time zone provided and adjusted to daylight savings according to that time zone.
    :type start_date_time: str
    :param expiration_date_time: Effective expiration date of the maintenance window in YYYY-MM-DD
     hh:mm format. The window will be created in the time zone provided and adjusted to daylight
     savings according to that time zone. Expiration date must be set to a future date. If not
     provided, it will be set to the maximum datetime 9999-12-31 23:59:59.
    :type expiration_date_time: str
    :param duration: Duration of the maintenance window in HH:mm format. If not provided, default
     value will be used based on maintenance scope provided. Example: 05:00.
    :type duration: str
    :param time_zone: Name of the timezone. List of timezones can be obtained by executing
     [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. Example: Pacific Standard Time, UTC,
     W. Europe Standard Time, Korea Standard Time, Cen. Australia Standard Time.
    :type time_zone: str
    :param recur_every: Rate at which a Maintenance window is expected to recur. The rate can be
     expressed as daily, weekly, or monthly schedules. Daily schedule are formatted as recurEvery:
     [Frequency as integer]['Day(s)']. If no frequency is provided, the default frequency is 1.
     Daily schedule examples are recurEvery: Day, recurEvery: 3Days.  Weekly schedule are formatted
     as recurEvery: [Frequency as integer]['Week(s)'] [Optional comma separated list of weekdays
     Monday-Sunday]. Weekly schedule examples are recurEvery: 3Weeks, recurEvery: Week
     Saturday,Sunday. Monthly schedules are formatted as [Frequency as integer]['Month(s)'] [Comma
     separated list of month days] or [Frequency as integer]['Month(s)'] [Week of Month (First,
     Second, Third, Fourth, Last)] [Weekday Monday-Sunday]. Monthly schedule examples are
     recurEvery: Month, recurEvery: 2Months, recurEvery: Month day23,day24, recurEvery: Month Last
     Sunday, recurEvery: Month Fourth Monday.
    :type recur_every: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'namespace': {'key': 'properties.namespace', 'type': 'str'},
        'extension_properties': {'key': 'properties.extensionProperties', 'type': '{str}'},
        'maintenance_scope': {'key': 'properties.maintenanceScope', 'type': 'str'},
        'visibility': {'key': 'properties.visibility', 'type': 'str'},
        'start_date_time': {'key': 'properties.maintenanceWindow.startDateTime', 'type': 'str'},
        'expiration_date_time': {'key': 'properties.maintenanceWindow.expirationDateTime', 'type': 'str'},
        'duration': {'key': 'properties.maintenanceWindow.duration', 'type': 'str'},
        'time_zone': {'key': 'properties.maintenanceWindow.timeZone', 'type': 'str'},
        'recur_every': {'key': 'properties.maintenanceWindow.recurEvery', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        namespace: Optional[str] = None,
        extension_properties: Optional[Dict[str, str]] = None,
        maintenance_scope: Optional[Union[str, "MaintenanceScope"]] = None,
        visibility: Optional[Union[str, "Visibility"]] = None,
        start_date_time: Optional[str] = None,
        expiration_date_time: Optional[str] = None,
        duration: Optional[str] = None,
        time_zone: Optional[str] = None,
        recur_every: Optional[str] = None,
        **kwargs
    ):
        super(MaintenanceConfiguration, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.namespace = namespace
        self.extension_properties = extension_properties
        self.maintenance_scope = maintenance_scope
        self.visibility = visibility
        self.start_date_time = start_date_time
        self.expiration_date_time = expiration_date_time
        self.duration = duration
        self.time_zone = time_zone
        self.recur_every = recur_every


class MaintenanceError(msrest.serialization.Model):
    """An error response received from the Azure Maintenance service.

    :param error: Details of the error.
    :type error: ~maintenance_client.models.ErrorDetails
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetails'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDetails"] = None,
        **kwargs
    ):
        super(MaintenanceError, self).__init__(**kwargs)
        self.error = error


class Operation(msrest.serialization.Model):
    """Represents an operation returned by the GetOperations request.

    :param name: Name of the operation.
    :type name: str
    :param display: Display name of the operation.
    :type display: ~maintenance_client.models.OperationInfo
    :param origin: Origin of the operation.
    :type origin: str
    :param properties: Properties of the operation.
    :type properties: object
    :param is_data_action: Indicates whether the operation is a data action.
    :type is_data_action: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationInfo'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationInfo"] = None,
        origin: Optional[str] = None,
        properties: Optional[object] = None,
        is_data_action: Optional[bool] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin
        self.properties = properties
        self.is_data_action = is_data_action


class OperationInfo(msrest.serialization.Model):
    """Information about an operation.

    :param provider: Name of the provider.
    :type provider: str
    :param resource: Name of the resource type.
    :type resource: str
    :param operation: Name of the operation.
    :type operation: str
    :param description: Description of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationInfo, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationsListResult(msrest.serialization.Model):
    """Result of the List Operations operation.

    :param value: A collection of operations.
    :type value: list[~maintenance_client.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        **kwargs
    ):
        super(OperationsListResult, self).__init__(**kwargs)
        self.value = value


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource. Possible values
     include: "User", "Application", "ManagedIdentity", "Key".
    :type created_by_type: str or ~maintenance_client.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: ~datetime.datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :type last_modified_by_type: str or ~maintenance_client.models.CreatedByType
    :param last_modified_at: The timestamp of resource last modification (UTC).
    :type last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at


class Update(msrest.serialization.Model):
    """Maintenance update on a resource.

    :param maintenance_scope: The impact area. Possible values include: "Host", "OSImage",
     "Extension", "InGuestPatch", "SQLDB", "SQLManagedInstance".
    :type maintenance_scope: str or ~maintenance_client.models.MaintenanceScope
    :param impact_type: The impact type. Possible values include: "None", "Freeze", "Restart",
     "Redeploy".
    :type impact_type: str or ~maintenance_client.models.ImpactType
    :param status: The status. Possible values include: "Pending", "InProgress", "Completed",
     "RetryNow", "RetryLater".
    :type status: str or ~maintenance_client.models.UpdateStatus
    :param impact_duration_in_sec: Duration of impact in seconds.
    :type impact_duration_in_sec: int
    :param not_before: Time when Azure will start force updates if not self-updated by customer
     before this time.
    :type not_before: ~datetime.datetime
    :param resource_id: The resourceId.
    :type resource_id: str
    """

    _attribute_map = {
        'maintenance_scope': {'key': 'maintenanceScope', 'type': 'str'},
        'impact_type': {'key': 'impactType', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'impact_duration_in_sec': {'key': 'impactDurationInSec', 'type': 'int'},
        'not_before': {'key': 'notBefore', 'type': 'iso-8601'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        maintenance_scope: Optional[Union[str, "MaintenanceScope"]] = None,
        impact_type: Optional[Union[str, "ImpactType"]] = None,
        status: Optional[Union[str, "UpdateStatus"]] = None,
        impact_duration_in_sec: Optional[int] = None,
        not_before: Optional[datetime.datetime] = None,
        resource_id: Optional[str] = None,
        **kwargs
    ):
        super(Update, self).__init__(**kwargs)
        self.maintenance_scope = maintenance_scope
        self.impact_type = impact_type
        self.status = status
        self.impact_duration_in_sec = impact_duration_in_sec
        self.not_before = not_before
        self.resource_id = resource_id
