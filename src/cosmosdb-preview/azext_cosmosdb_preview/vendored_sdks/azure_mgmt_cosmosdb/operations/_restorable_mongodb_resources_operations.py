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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class RestorableMongodbResourcesOperations(object):
    """RestorableMongodbResourcesOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for this operation. Constant value: "2020-06-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-06-01-preview"

        self.config = config

    def list(
            self, location, instance_id, restore_location=None, restore_timestamp_in_utc=None, custom_headers=None, raw=False, **operation_config):
        """Return a list of database and collection combo that exist on the
        account at the given timestamp and location. This helps in scenarios to
        validate what resources exist at given timestamp and location. This API
        requires
        'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/*/read'
        permission.

        :param location: Cosmos DB region, with spaces between words and each
         word capitalized.
        :type location: str
        :param instance_id: The instanceId GUID of a restorable database
         account.
        :type instance_id: str
        :param restore_location: The location where the restorable resources
         are located.
        :type restore_location: str
        :param restore_timestamp_in_utc: The timestamp when the restorable
         resources existed.
        :type restore_timestamp_in_utc: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DatabaseRestoreResource
        :rtype:
         ~azure.mgmt.cosmosdb.models.DatabaseRestoreResourcePaged[~azure.mgmt.cosmosdb.models.DatabaseRestoreResource]
        :raises:
         :class:`DefaultErrorResponseException<azure.mgmt.cosmosdb.models.DefaultErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
                    'location': self._serialize.url("location", location, 'str'),
                    'instanceId': self._serialize.url("instance_id", instance_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)
                if restore_location is not None:
                    query_parameters['restoreLocation'] = self._serialize.query("restore_location", restore_location, 'str')
                if restore_timestamp_in_utc is not None:
                    query_parameters['restoreTimestampInUtc'] = self._serialize.query("restore_timestamp_in_utc", restore_timestamp_in_utc, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.DefaultErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.DatabaseRestoreResourcePaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts/{instanceId}/restorableMongodbResources'}
