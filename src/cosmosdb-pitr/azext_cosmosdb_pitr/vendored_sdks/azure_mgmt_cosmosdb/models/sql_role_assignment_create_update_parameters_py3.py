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


class SqlRoleAssignmentCreateUpdateParameters(Model):
    """Parameters to create and update an Azure Cosmos DB SQL Role Assignment.

    :param role_definition_id: The unique identifier for the associated Role
     Definition.
    :type role_definition_id: str
    :param scope: The data plane resource path for which access is being
     granted through this Role Assignment.
    :type scope: str
    :param principal_id: The unique identifier for the associated AAD
     principal in the AAD graph to which access is being granted through this
     Role Assignment. Tenant ID for the principal is inferred using the tenant
     associated with the subscription.
    :type principal_id: str
    """

    _attribute_map = {
        'role_definition_id': {'key': 'properties.roleDefinitionId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'principal_id': {'key': 'properties.principalId', 'type': 'str'},
    }

    def __init__(self, *, role_definition_id: str=None, scope: str=None, principal_id: str=None, **kwargs) -> None:
        super(SqlRoleAssignmentCreateUpdateParameters, self).__init__(**kwargs)
        self.role_definition_id = role_definition_id
        self.scope = scope
        self.principal_id = principal_id
