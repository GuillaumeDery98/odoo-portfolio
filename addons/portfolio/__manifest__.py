{
    'name': "Guillaume Dery Portfolio",
    'version': '1.0',
    'depends': ['base'],
    'author': "Guillaume Dery",
    'application': True,
    'category': 'Human Resources',
    'description': """
    Guillame Dery Portfolio for try Odoo addons development
    """,
    # data files always loaded at installation
    'data': [
        'views/portfolio_companies.xml',
        'views/portfolio_menu.xml',
        'data/ir.model.access.csv'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
}
