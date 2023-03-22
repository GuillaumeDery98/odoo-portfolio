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
        'views/companies/portfolio_companies.xml',
        'views/projects/portfolio_projects.xml',
        'views/projects/portfolio_screenshots.xml',
        'views/portfolio_menu.xml',
        'data/ir.model.access.csv'
    ],
    'assets': {
        'web.assets_common': [
            'portfolio/static/src/css/portfolio.css',
        ],
    },
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
}
