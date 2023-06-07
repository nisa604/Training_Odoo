from odoo import models, fields, api, _
from odoo.exceptions import UserError

class BusRoute(models.Model):
    _name = 'bus.route'
    _description="Rute yang ditembuh bus"

    name = fields.Char(string='Name')