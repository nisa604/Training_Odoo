from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResBus(models.Model):
    _name = 'res.bus'
    _description = 'Mobil Bus'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    capacity = fields.Integer(string='Capacity')
    image = fields.Binary(string='Image')
    state = fields.Selection(
        selection=[
            ("draft","Draft"),
            ("ready","Ready"),
            ("mt","Maintance"),
            ("depr","Deprecated")
            ], 
        string='Status', 
        default='draft'
        )