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

from msrest.serialization import Model


class DatabaseAccountUpdateParameters(Model):
    """Parameters for patching Azure Cosmos DB database account properties.

    :param tags:
    :type tags: dict[str, str]
    :param location: The location of the resource group to which the resource
     belongs.
    :type location: str
    :param consistency_policy: The consistency policy for the Cosmos DB
     account.
    :type consistency_policy: ~azure.mgmt.cosmosdb.models.ConsistencyPolicy
    :param locations: An array that contains the georeplication locations
     enabled for the Cosmos DB account.
    :type locations: list[~azure.mgmt.cosmosdb.models.Location]
    :param ip_rules: List of IpRules.
    :type ip_rules: list[~azure.mgmt.cosmosdb.models.IpAddressOrRange]
    :param is_virtual_network_filter_enabled: Flag to indicate whether to
     enable/disable Virtual Network ACL rules.
    :type is_virtual_network_filter_enabled: bool
    :param enable_automatic_failover: Enables automatic failover of the write
     region in the rare event that the region is unavailable due to an outage.
     Automatic failover will result in a new write region for the account and
     is chosen based on the failover priorities configured for the account.
    :type enable_automatic_failover: bool
    :param capabilities: List of Cosmos DB capabilities for the account
    :type capabilities: list[~azure.mgmt.cosmosdb.models.Capability]
    :param virtual_network_rules: List of Virtual Network ACL rules configured
     for the Cosmos DB account.
    :type virtual_network_rules:
     list[~azure.mgmt.cosmosdb.models.VirtualNetworkRule]
    :param enable_multiple_write_locations: Enables the account to write in
     multiple locations
    :type enable_multiple_write_locations: bool
    :param enable_cassandra_connector: Enables the cassandra connector on the
     Cosmos DB C* account
    :type enable_cassandra_connector: bool
    :param connector_offer: The cassandra connector offer type for the Cosmos
     DB database C* account. Possible values include: 'Small'
    :type connector_offer: str or ~azure.mgmt.cosmosdb.models.ConnectorOffer
    :param disable_key_based_metadata_write_access: Disable write operations
     on metadata resources (databases, containers, throughput) via account keys
    :type disable_key_based_metadata_write_access: bool
    :param key_vault_key_uri: The URI of the key vault
    :type key_vault_key_uri: str
    :param public_network_access: Whether requests from Public Network are
     allowed. Possible values include: 'Enabled', 'Disabled'
    :type public_network_access: str or
     ~azure.mgmt.cosmosdb.models.PublicNetworkAccess
    :param enable_free_tier: Flag to indicate whether Free Tier is enabled.
    :type enable_free_tier: bool
    :param api_properties: API specific properties. Currently, supported only
     for MongoDB API.
    :type api_properties: ~azure.mgmt.cosmosdb.models.ApiProperties
    :param enable_analytical_storage: Flag to indicate whether to enable
     storage analytics.
    :type enable_analytical_storage: bool
    :param backup_policy: The object representing the policy for taking
     backups on an account.
    :type backup_policy: ~azure.mgmt.cosmosdb.models.BackupPolicy
    :param cors: The CORS policy for the Cosmos DB database account.
    :type cors: list[~azure.mgmt.cosmosdb.models.CorsPolicy]
    :param identity:
    :type identity: ~azure.mgmt.cosmosdb.models.ManagedServiceIdentity
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'consistency_policy': {'key': 'properties.consistencyPolicy', 'type': 'ConsistencyPolicy'},
        'locations': {'key': 'properties.locations', 'type': '[Location]'},
        'ip_rules': {'key': 'properties.ipRules', 'type': '[IpAddressOrRange]'},
        'is_virtual_network_filter_enabled': {'key': 'properties.isVirtualNetworkFilterEnabled', 'type': 'bool'},
        'enable_automatic_failover': {'key': 'properties.enableAutomaticFailover', 'type': 'bool'},
        'capabilities': {'key': 'properties.capabilities', 'type': '[Capability]'},
        'virtual_network_rules': {'key': 'properties.virtualNetworkRules', 'type': '[VirtualNetworkRule]'},
        'enable_multiple_write_locations': {'key': 'properties.enableMultipleWriteLocations', 'type': 'bool'},
        'enable_cassandra_connector': {'key': 'properties.enableCassandraConnector', 'type': 'bool'},
        'connector_offer': {'key': 'properties.connectorOffer', 'type': 'str'},
        'disable_key_based_metadata_write_access': {'key': 'properties.disableKeyBasedMetadataWriteAccess', 'type': 'bool'},
        'key_vault_key_uri': {'key': 'properties.keyVaultKeyUri', 'type': 'str'},
        'public_network_access': {'key': 'properties.publicNetworkAccess', 'type': 'str'},
        'enable_free_tier': {'key': 'properties.enableFreeTier', 'type': 'bool'},
        'api_properties': {'key': 'properties.apiProperties', 'type': 'ApiProperties'},
        'enable_analytical_storage': {'key': 'properties.enableAnalyticalStorage', 'type': 'bool'},
        'backup_policy': {'key': 'properties.backupPolicy', 'type': 'BackupPolicy'},
        'cors': {'key': 'properties.cors', 'type': '[CorsPolicy]'},
        'identity': {'key': 'identity', 'type': 'ManagedServiceIdentity'},
    }

    def __init__(self, **kwargs):
        super(DatabaseAccountUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs.get('location', None)
        self.consistency_policy = kwargs.get('consistency_policy', None)
        self.locations = kwargs.get('locations', None)
        self.ip_rules = kwargs.get('ip_rules', None)
        self.is_virtual_network_filter_enabled = kwargs.get('is_virtual_network_filter_enabled', None)
        self.enable_automatic_failover = kwargs.get('enable_automatic_failover', None)
        self.capabilities = kwargs.get('capabilities', None)
        self.virtual_network_rules = kwargs.get('virtual_network_rules', None)
        self.enable_multiple_write_locations = kwargs.get('enable_multiple_write_locations', None)
        self.enable_cassandra_connector = kwargs.get('enable_cassandra_connector', None)
        self.connector_offer = kwargs.get('connector_offer', None)
        self.disable_key_based_metadata_write_access = kwargs.get('disable_key_based_metadata_write_access', None)
        self.key_vault_key_uri = kwargs.get('key_vault_key_uri', None)
        self.public_network_access = kwargs.get('public_network_access', None)
        self.enable_free_tier = kwargs.get('enable_free_tier', None)
        self.api_properties = kwargs.get('api_properties', None)
        self.enable_analytical_storage = kwargs.get('enable_analytical_storage', None)
        self.backup_policy = kwargs.get('backup_policy', None)
        self.cors = kwargs.get('cors', None)
        self.identity = kwargs.get('identity', None)
