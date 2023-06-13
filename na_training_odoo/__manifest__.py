# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-06-07 12:06:56
# @Last Modified by:   Your name
# @Last Modified time: 2023-06-07 14:20:59

{
    'name': "Training Odoo (Nisa)",

    'summary': """
        Modul Transportasi Management""",

    'description': """
        platform logistik menggunakan teknologi yang berfungsi untuk merencanakan, melaksanakan, dan mengoptimalkan pergerakan sebuah barang, baik masuk maupun keluar, serta memastikan pengiriman sesuai berdasarkan dokumentasi yang tersedia.
    """,

    'author': "Nurul Anisah",
    'website': "https://www.linkedin.com/in/nurul-anisah-07b81721b/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'mail'],

    # always loaded
    'data': [
        'data/data.xml',
        'data/sequence.xml',
        'data/action_server.xml',
        'security/ir.model.access.csv',
        'views/menuitems.xml',
        'views/employee_view.xml',
        'views/res_passenger_view.xml',
        'views/res_bus_view.xml',
        'views/bus_schedule_view.xml',
        'views/bus_route_view.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
