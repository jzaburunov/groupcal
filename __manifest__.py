# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
{
    'name': "depyl_cal",

    'summary': 'Depyl Groupped calendar',

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
    'depends': ['web','base','web_calendar'],
    #'depends': ['sale_stock'],

    # Qweb templates
    #'qweb': ['templates.xml'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'templates.xml',
        'calendar.xml',
        #'data.xml'
    ],

    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
        #'data.xml',
    ],
    'application': True,
    # TODO IN calendar view occurs
    #'auto_install': True
}
# {
#     'name' : 'depyl_cal',

#     'summary': 'Salon management calendar',

#     'description': 'TODO',

#     'author': 'jzaburunov',

#     'website': 'TODO',

#     'category': 'Uncategorized',

#     'version': '0.1',

#     'depends': ['web', 'base', 'web_calendar'],

#     #'qweb': []

#     'data': [
#         'calendar.xml'
#     ],

#     application: True
# }
