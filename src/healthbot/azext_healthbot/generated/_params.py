# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group


def load_arguments(self, _):

    with self.argument_context('healthbot list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('healthbot show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('bot_name', options_list=['--name', '-n', '--bot-name'], type=str, help='The name of the Bot '
                   'resource.', id_part='name')

    with self.argument_context('healthbot create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('bot_name', options_list=['--name', '-n', '--bot-name'], type=str, help='The name of the Bot resource.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('sku', arg_type=get_enum_type(['F0', 'S1', 'C0']), help='The name of the HealthBot SKU',
                   arg_group='Sku')

    with self.argument_context('healthbot update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('bot_name', options_list=['--name', '-n', '--bot-name'], type=str, help='The name of the Bot resource.', id_part='name')
        c.argument('tags', tags_type)
        c.argument('sku', arg_type=get_enum_type(['F0', 'S1', 'C0']), help='The name of the HealthBot SKU',
                   arg_group='Sku')

    with self.argument_context('healthbot delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('bot_name', options_list=['--name', '-n', '--bot-name'], type=str, help='The name of the Bot '
                   'resource.', id_part='name')

    with self.argument_context('healthbot wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('bot_name', options_list=['--name', '-n', '--bot-name'], type=str, help='The name of the Bot '
                   'resource.', id_part='name')