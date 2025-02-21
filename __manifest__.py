# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Contract - Document',
    'version': '1.0',
    'category': 'Business Management',
    'sequence': 5,
    'summary': 'Contract and Document Management streamlines organization, tracking, and compliance.',
    'author': 'Kariat Nguyen',
    'description': "Manage contracts and related documents efficiently.",
    'website': 'https://www.odoo.com',
    'depends': ['base'], 
    'auto_install': False,
    'installable': True,
    'application': True,
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/view.xml"
    ],
}
