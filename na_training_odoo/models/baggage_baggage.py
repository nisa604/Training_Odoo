# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-06-08 13:37:01
# @Last Modified by:   Your name
# @Last Modified time: 2023-06-08 13:45:36
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Baggage(models.Model):
    _name = 'baggage.baggage'
    _description = 'Baggage'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    schedule_id = fields.Many2one(
        comodel_name='bus.schedule',
        string='Schedule',
    )