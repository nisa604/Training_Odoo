from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Subject(models.Model):
    _name = 'subject.subject'
    _description="Mata kuliah yg tersedia"

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    lecturer_id = fields.Many2one(
        comodel_name='res.partner',
        string="Lecturer",
    )