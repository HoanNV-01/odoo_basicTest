{
    'name': 'Links',
    'category': 'Marketing',
    'description': """
Create short and trackable URLs.
=====================================================

        """,
    'version': '1.0',
    'author': 'Dom. Kariat Nguyen',
    'depends': ['base'],
    'summary': 'Manager links',
    'installable': True,
    'application': True,
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/links_views.xml',
    ],
}