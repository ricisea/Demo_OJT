# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Latihan',
    'category': 'Sales',
    'author': 'Mak',
    'version': '1.0',
    'website': 'http://www.solvera.id/',
    'description': """
       hanya untuk latihan
    """,
    'data': [
	'views/sale_order_views.xml',
    'views/dp_form.xml',
    'report/purchase_reports.xml',
    'report/purchase_order_templates.xml',


    ],
    "depends": [
        "sale","sale_management","purchase"
    ],
    'installable': True,
    "images":['static/logo.png'],
}
