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

from .backup_policy import BackupPolicy


class PeriodicModeBackupPolicy(BackupPolicy):
    """The object representing periodic mode backup policy.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param periodic_mode_properties: Configuration values for periodic mode
     backup
    :type periodic_mode_properties:
     ~azure.mgmt.cosmosdb.models.PeriodicModeProperties
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'periodic_mode_properties': {'key': 'periodicModeProperties', 'type': 'PeriodicModeProperties'},
    }

    def __init__(self, **kwargs):
        super(PeriodicModeBackupPolicy, self).__init__(**kwargs)
        self.periodic_mode_properties = kwargs.get('periodic_mode_properties', None)
        self.type = 'Periodic'
