# -*- coding: utf-8 -*-
{
    'name': "Training Academy (Nisa)",

    'summary': """
        Modul Mahasiswa""",

    'description': """
        Mahasiswa dapat memilih dan melihat matakuliah beserta dosen yang mengajarnya
    """,

    'author': "NTI",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menuitems.xml',
        'views/subject.xml',
        'views/res_partner.xml',
        'views/class_view.xml',
        'report/report.xml',
        'report/report_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
