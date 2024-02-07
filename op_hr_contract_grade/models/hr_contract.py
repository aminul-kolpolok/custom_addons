'''
Created on Jun 15, 2023

@author: Odoopedia
'''
from odoo import models, fields


class Contract(models.Model):
    _inherit = 'hr.contract'
        
    grade = fields.Many2one('hr.contract.grade', string="Emp. Grade")
  