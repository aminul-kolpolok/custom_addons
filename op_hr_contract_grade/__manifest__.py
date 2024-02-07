# -*- coding: utf-8 -*-

{
    'name': 'Employee Contract Grade',
    'author': 'Odoopedia',
    'version': '16.0',
    'category': 'Human Resources',
    'sequence': 85,
    'summary': """Employee Contract Grade
                  Employee Grade
                  Grade system
                  Grade level
                  Grade salary
                  Grade structure
                  Grade scale""",
    'maintainer': 'Odoopedia',
    'website': 'https://www.odoopedia.com',
    'description': """
        This module adds a grade drop-down list to the employee contract form, allowing users to easily assign a contract grade to each employee.""",
    'license': 'OPL-1',
    'support': 'contact@odoopedia.com',
    'depends': ['hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_contract_views.xml'
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
