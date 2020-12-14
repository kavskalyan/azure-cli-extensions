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

from .arm_resource_properties_py3 import ARMResourceProperties


class SqlStoredProcedureGetResults(ARMResourceProperties):
    """An Azure Cosmos DB storedProcedure.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The unique resource identifier of the ARM resource.
    :vartype id: str
    :ivar name: The name of the ARM resource.
    :vartype name: str
    :ivar type: The type of Azure resource.
    :vartype type: str
    :param location: The location of the resource group to which the resource
     belongs.
    :type location: str
    :param tags:
    :type tags: dict[str, str]
    :param identity:
    :type identity: ~azure.mgmt.cosmosdb.models.ManagedServiceIdentity
    :param resource:
    :type resource:
     ~azure.mgmt.cosmosdb.models.SqlStoredProcedureGetPropertiesResource
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
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'ManagedServiceIdentity'},
        'resource': {'key': 'properties.resource', 'type': 'SqlStoredProcedureGetPropertiesResource'},
    }

    def __init__(self, *, location: str=None, tags=None, identity=None, resource=None, **kwargs) -> None:
        super(SqlStoredProcedureGetResults, self).__init__(location=location, tags=tags, identity=identity, **kwargs)
        self.resource = resource
