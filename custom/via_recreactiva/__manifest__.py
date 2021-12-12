# -*- coding: utf-8 -*-
# Copyright © Via Recreactiva - All Rights Reserved
# Author      Christian Daniel Medina Herrera

{
    'name': 'Via Recreactiva',
    'version': '1.0',
    'summary': 'Administracion & Control',
    'sequence': 10,
    'description': """
Via Recreativa
====================
Este es el modulo oficial para la via recreactiva

Dentro de este modulo se encuentran los registros necesarios para los guias de la via para llevar el control absoluto.
    """,
    'category': 'Management/Control',
    'website': '',
    'images': [],
    'depends': ['mail'],
    'data': [
        'data/ir.module.category.csv',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/reporte_accidentes_view.xml',
        'views/menu.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web._assets_primary_variables': [
        ],
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
        ],
        'web.assets_tests': [
        ],
        'web.qunit_suite_tests': [
        ],
        'web.assets_qweb': [
        ],
    },
    'license': 'LGPL-3',
}
