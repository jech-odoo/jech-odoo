{
    'name': 'Real Estate',
    'application': True,
    'installable': True,
    'depends': ['base', 'website'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_menu.xml',
        'views/estate_view.xml',
        'wizard/property_view.xml',
        'views/template.xml',
        'data/estate_data.xml',
    ],
    'license': 'LGPL-3',
}
