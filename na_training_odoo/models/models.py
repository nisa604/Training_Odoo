# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class na_training_odoo(models.Model):
#     _name = 'na_training_odoo.na_training_odoo'
#     _description = 'na_training_odoo.na_training_odoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
