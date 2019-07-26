# coding: utf-8
# © 2019 Aron Langat
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'NCF',
    'summary': 'factory system',
    'version': '1.0',
    'category': 'Custom',
    'author': 'Aron Langat',
    'website': 'https://sunflowerweb.nl',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'views/menu.xml',
        'views/farmer_registration.xml',
        'views/berry_collection.xml',
        'views/mbuni_collection.xml',
        'views/employees.xml',
        'views/petty_cash.xml',
        'report/berry_report.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True
}
