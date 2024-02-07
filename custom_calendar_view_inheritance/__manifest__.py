# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Calendar View update',
    'version': '1.1',
    # 'sequence': 165,
    'depends': [],
    'summary': "Schedule employees' meetings",
    'description': """
This is a full-featured calendar system.
========================================

It supports:
------------
    - Calendar of events
    - Recurring events

If you need to manage your meetings, you should install the CRM module.
    """,
    'category': 'Productivity/Calendar',
    'demo': [
        # 'data/calendar_demo.xml'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/calendar_security.xml',
        # 'data/calendar_cron.xml',
        # 'data/mail_template_data.xml',
        # 'data/calendar_data.xml',
        # 'data/mail_activity_type_data.xml',
        # 'data/mail_message_subtype_data.xml',
        # 'views/mail_activity_views.xml',
        'views/custom_inheritance_view.xml',
        # 'views/calendar_views.xml',
        # 'views/res_partner_views.xml',
        # 'wizard/calendar_provider_config.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
