'''
Created on Jun 15, 2023

@author: Odoopedia
'''
from odoo import models, fields


class HrContractGrade(models.Model):
    _name = 'hr.contract.grade'
    _description = 'Grade'
    _order='name'

    name = fields.Char('Emp. Grade', help='The salary structure grade', required=True)

    _sql_constraints = [('name_unique', 'unique(name)', 'grade should be unique!')]