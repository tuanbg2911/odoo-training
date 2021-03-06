{
    'name': 'Sale Training',
    'version': '1.1',
    'category': '',
    'summary': 'Sale Training',
    'description': """Tags đơn hàng""",
    'category': 'Application',
    'website': 'https://odoo.vn',
    'depends': ['sale', 'base'],
    'data': ['views/sale_order_tags_view.xml',
             'views/sale_orders_views.xml',
             'views/customize_search.xml',
             'views/res_partner.xml',
             'wizards/tags_wizard.xml',
             'security/sale_order_tags_security.xml',
             'security/ir.model.access.csv',
             'reports/report_printer.xml',
             'reports/report_template.xml'],
    'demo': [],

}
