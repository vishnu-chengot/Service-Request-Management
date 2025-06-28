{
    'name': 'Service Request Management',
    'version': '16.0.1.0.0',
    'category': 'Services',
    'summary': 'Manage service requests with workflow and tracking',
    'description': """
        Service Request Management Module
        ================================
        This module provides:
        * Service request creation and management
        * Customer communication
        * Reporting and analytics
    """,
    'author': 'vishnu.chengot',
    'website': '',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/service_request_view.xml',
        'data/assign_emai_template.xml',
        'views/dashboard_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            "service_request_management/static/src/js/request_dashboard.js",
            "service_request_management/static/src/css/request_dashboard.css",
            "service_request_management/static/src/xml/request_dashboard.xml",
    ]},
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}