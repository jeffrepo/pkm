{
    'name': 'PKM',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Formato de cotización personalizado para órdenes de venta',
    'description': """
        Este módulo proporciona un formato de cotización personalizado para las órdenes de venta.
    """,
    'author': 'Your Name',
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
        'views/report_templates.xml',
        'report/cotizacion_sale_order.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'pkm/static/src/img/*.png',
            'pkm/static/src/img/*.jpg',
            'pkm/static/src/img/*.jpeg',
        ],
    },
    'installable': True,
    'application': False,
}
