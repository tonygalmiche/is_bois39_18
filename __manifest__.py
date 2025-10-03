# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 18 pour Bois 39',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 18 pour Bois 39
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'account',
        'l10n_fr',
        'l10n_fr_account',
        'contacts',
        'web_chatter_position',
        'web_m2x_options',
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    "assets": {
        'web.assets_backend': [
            'is_bois39_18/static/src/**/*',
         ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
