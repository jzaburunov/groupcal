# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
{
    'name': "groupcal",

    'summary': 'Groupped calendar view',

    'description': """
        TODO
    """,

    'author': "JZ",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web', 'base', 'web_calendar'],

    # always loaded
    'data': [
        'calendar.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],

    'application': True,
}
