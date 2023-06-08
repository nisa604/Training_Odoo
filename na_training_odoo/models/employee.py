from odoo import models, fields, api, _
from odoo.exceptions import UserError

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    is_driver = fields.Boolean(string='Is Driver')