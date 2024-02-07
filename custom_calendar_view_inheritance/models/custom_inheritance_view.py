from odoo import models, fields

class HrLeaveReportCalendarCustom(models.Model):
    _inherit = 'hr.leave.report.calendar'

    # Add your custom fields here
    your_custom_field = fields.Char(string="Your Custom Field")