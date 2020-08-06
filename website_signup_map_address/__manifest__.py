# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2018 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Website Signup Map Address',
    'category': 'Website',
    'summary': 'Website Signup Map Address',

    'version': '0.1',
    'description': """
Website Signup Map Address
==================
        This module allows store address into Contact(partner) while register of the user.
        """,

    'author': 'Odoo Helper',
    'license': 'AGPL-3',

    'depends': [
        'base','website','contacts'
        ],
    'data': [
        'views/assets.xml',
        'views/res_partner.xml',
        'views/template.xml',
    ],
    'images': ['images/OdooHelper.jpg'],
    'price': 10.28,
    'currency': 'USD',

    'installable': True,
    'application': False
}
