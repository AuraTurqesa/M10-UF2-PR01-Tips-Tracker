{
    'name': "Gestor de Propinas",
    'version': "1.0",
    'category': "Human Resources",
    'summary': "Gestión y seguimiento de propinas de empleados",
    'description': """
        Este módulo permite gestionar y hacer seguimiento de las propinas de los empleados.
        Características:
        - Registro detallado de propinas
        - Seguimiento del estado (borrador, confirmado, pagado)
        - Análisis con gráficos y vistas pivot
        - Generación de informes PDF
    """,
    'author': 'Sergi Saravia',
    'website': 'https://www.sergisaravia.com',
    'depends': ['hr'],
    'data': [
        'security/security.xml',
        'views/tip_views.xml',
        'views/tip_graph_views.xml',
        'reports/tip_report.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 