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


class SqlStoredProcedureGetPropertiesResource(Model):
    """SqlStoredProcedureGetPropertiesResource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Name of the Cosmos DB SQL storedProcedure
    :type id: str
    :param body: Body of the Stored Procedure
    :type body: str
    :ivar _rid: A system generated property. A unique identifier.
    :vartype _rid: str
    :ivar _ts: A system generated property that denotes the last updated
     timestamp of the resource.
    :vartype _ts: object
    :ivar _etag: A system generated property representing the resource etag
     required for optimistic concurrency control.
    :vartype _etag: str
    """

    _validation = {
        'id': {'required': True},
        '_rid': {'readonly': True},
        '_ts': {'readonly': True},
        '_etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'body': {'key': 'body', 'type': 'str'},
        '_rid': {'key': '_rid', 'type': 'str'},
        '_ts': {'key': '_ts', 'type': 'object'},
        '_etag': {'key': '_etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SqlStoredProcedureGetPropertiesResource, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.body = kwargs.get('body', None)
        self._rid = None
        self._ts = None
        self._etag = None
