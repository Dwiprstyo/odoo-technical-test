{
    'name': "Material",
    'summary': """Material""",
    'description': """Material""",
    'author': "Muhammad Dwi Prasetyo",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/supplier.xml',
        'data/material.xml',
        'views/menuitems.xml',
        'views/material.views.xml',
        'views/supplier.views.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}