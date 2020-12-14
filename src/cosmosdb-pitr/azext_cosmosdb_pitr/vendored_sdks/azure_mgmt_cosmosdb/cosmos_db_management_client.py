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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.database_accounts_operations import DatabaseAccountsOperations
from .operations.operations import Operations
from .operations.database_operations import DatabaseOperations
from .operations.collection_operations import CollectionOperations
from .operations.collection_region_operations import CollectionRegionOperations
from .operations.database_account_region_operations import DatabaseAccountRegionOperations
from .operations.percentile_source_target_operations import PercentileSourceTargetOperations
from .operations.percentile_target_operations import PercentileTargetOperations
from .operations.percentile_operations import PercentileOperations
from .operations.collection_partition_region_operations import CollectionPartitionRegionOperations
from .operations.collection_partition_operations import CollectionPartitionOperations
from .operations.partition_key_range_id_operations import PartitionKeyRangeIdOperations
from .operations.partition_key_range_id_region_operations import PartitionKeyRangeIdRegionOperations
from .operations.sql_resources_operations import SqlResourcesOperations
from .operations.mongo_db_resources_operations import MongoDBResourcesOperations
from .operations.table_resources_operations import TableResourcesOperations
from .operations.cassandra_resources_operations import CassandraResourcesOperations
from .operations.gremlin_resources_operations import GremlinResourcesOperations
from .operations.restorable_database_accounts_operations import RestorableDatabaseAccountsOperations
from .operations.notebook_workspaces_operations import NotebookWorkspacesOperations
from .operations.restorable_sql_databases_operations import RestorableSqlDatabasesOperations
from .operations.restorable_sql_containers_operations import RestorableSqlContainersOperations
from .operations.restorable_sql_resources_operations import RestorableSqlResourcesOperations
from .operations.restorable_mongodb_databases_operations import RestorableMongodbDatabasesOperations
from .operations.restorable_mongodb_collections_operations import RestorableMongodbCollectionsOperations
from .operations.restorable_mongodb_resources_operations import RestorableMongodbResourcesOperations
from .operations.private_link_resources_operations import PrivateLinkResourcesOperations
from .operations.private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from . import models


class CosmosDBManagementClientConfiguration(AzureConfiguration):
    """Configuration for CosmosDBManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(CosmosDBManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-cosmosdb/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class CosmosDBManagementClient(SDKClient):
    """CosmosDBManagementClient

    :ivar config: Configuration for client.
    :vartype config: CosmosDBManagementClientConfiguration

    :ivar database_accounts: DatabaseAccounts operations
    :vartype database_accounts: azure.mgmt.cosmosdb.operations.DatabaseAccountsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.cosmosdb.operations.Operations
    :ivar database: Database operations
    :vartype database: azure.mgmt.cosmosdb.operations.DatabaseOperations
    :ivar collection: Collection operations
    :vartype collection: azure.mgmt.cosmosdb.operations.CollectionOperations
    :ivar collection_region: CollectionRegion operations
    :vartype collection_region: azure.mgmt.cosmosdb.operations.CollectionRegionOperations
    :ivar database_account_region: DatabaseAccountRegion operations
    :vartype database_account_region: azure.mgmt.cosmosdb.operations.DatabaseAccountRegionOperations
    :ivar percentile_source_target: PercentileSourceTarget operations
    :vartype percentile_source_target: azure.mgmt.cosmosdb.operations.PercentileSourceTargetOperations
    :ivar percentile_target: PercentileTarget operations
    :vartype percentile_target: azure.mgmt.cosmosdb.operations.PercentileTargetOperations
    :ivar percentile: Percentile operations
    :vartype percentile: azure.mgmt.cosmosdb.operations.PercentileOperations
    :ivar collection_partition_region: CollectionPartitionRegion operations
    :vartype collection_partition_region: azure.mgmt.cosmosdb.operations.CollectionPartitionRegionOperations
    :ivar collection_partition: CollectionPartition operations
    :vartype collection_partition: azure.mgmt.cosmosdb.operations.CollectionPartitionOperations
    :ivar partition_key_range_id: PartitionKeyRangeId operations
    :vartype partition_key_range_id: azure.mgmt.cosmosdb.operations.PartitionKeyRangeIdOperations
    :ivar partition_key_range_id_region: PartitionKeyRangeIdRegion operations
    :vartype partition_key_range_id_region: azure.mgmt.cosmosdb.operations.PartitionKeyRangeIdRegionOperations
    :ivar sql_resources: SqlResources operations
    :vartype sql_resources: azure.mgmt.cosmosdb.operations.SqlResourcesOperations
    :ivar mongo_db_resources: MongoDBResources operations
    :vartype mongo_db_resources: azure.mgmt.cosmosdb.operations.MongoDBResourcesOperations
    :ivar table_resources: TableResources operations
    :vartype table_resources: azure.mgmt.cosmosdb.operations.TableResourcesOperations
    :ivar cassandra_resources: CassandraResources operations
    :vartype cassandra_resources: azure.mgmt.cosmosdb.operations.CassandraResourcesOperations
    :ivar gremlin_resources: GremlinResources operations
    :vartype gremlin_resources: azure.mgmt.cosmosdb.operations.GremlinResourcesOperations
    :ivar restorable_database_accounts: RestorableDatabaseAccounts operations
    :vartype restorable_database_accounts: azure.mgmt.cosmosdb.operations.RestorableDatabaseAccountsOperations
    :ivar notebook_workspaces: NotebookWorkspaces operations
    :vartype notebook_workspaces: azure.mgmt.cosmosdb.operations.NotebookWorkspacesOperations
    :ivar restorable_sql_databases: RestorableSqlDatabases operations
    :vartype restorable_sql_databases: azure.mgmt.cosmosdb.operations.RestorableSqlDatabasesOperations
    :ivar restorable_sql_containers: RestorableSqlContainers operations
    :vartype restorable_sql_containers: azure.mgmt.cosmosdb.operations.RestorableSqlContainersOperations
    :ivar restorable_sql_resources: RestorableSqlResources operations
    :vartype restorable_sql_resources: azure.mgmt.cosmosdb.operations.RestorableSqlResourcesOperations
    :ivar restorable_mongodb_databases: RestorableMongodbDatabases operations
    :vartype restorable_mongodb_databases: azure.mgmt.cosmosdb.operations.RestorableMongodbDatabasesOperations
    :ivar restorable_mongodb_collections: RestorableMongodbCollections operations
    :vartype restorable_mongodb_collections: azure.mgmt.cosmosdb.operations.RestorableMongodbCollectionsOperations
    :ivar restorable_mongodb_resources: RestorableMongodbResources operations
    :vartype restorable_mongodb_resources: azure.mgmt.cosmosdb.operations.RestorableMongodbResourcesOperations
    :ivar private_link_resources: PrivateLinkResources operations
    :vartype private_link_resources: azure.mgmt.cosmosdb.operations.PrivateLinkResourcesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnections operations
    :vartype private_endpoint_connections: azure.mgmt.cosmosdb.operations.PrivateEndpointConnectionsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = CosmosDBManagementClientConfiguration(credentials, subscription_id, base_url)
        super(CosmosDBManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.database_accounts = DatabaseAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.database = DatabaseOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.collection = CollectionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.collection_region = CollectionRegionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.database_account_region = DatabaseAccountRegionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.percentile_source_target = PercentileSourceTargetOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.percentile_target = PercentileTargetOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.percentile = PercentileOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.collection_partition_region = CollectionPartitionRegionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.collection_partition = CollectionPartitionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.partition_key_range_id = PartitionKeyRangeIdOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.partition_key_range_id_region = PartitionKeyRangeIdRegionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_resources = SqlResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.mongo_db_resources = MongoDBResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.table_resources = TableResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.cassandra_resources = CassandraResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.gremlin_resources = GremlinResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.restorable_database_accounts = RestorableDatabaseAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.notebook_workspaces = NotebookWorkspacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.restorable_sql_databases = RestorableSqlDatabasesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.restorable_sql_containers = RestorableSqlContainersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.restorable_sql_resources = RestorableSqlResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.restorable_mongodb_databases = RestorableMongodbDatabasesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.restorable_mongodb_collections = RestorableMongodbCollectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.restorable_mongodb_resources = RestorableMongodbResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
