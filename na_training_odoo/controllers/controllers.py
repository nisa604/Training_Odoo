# -*- coding: utf-8 -*-
# from odoo import http


# class NaTrainingOdoo(http.Controller):
#     @http.route('/na_training_odoo/na_training_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/na_training_odoo/na_training_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('na_training_odoo.listing', {
#             'root': '/na_training_odoo/na_training_odoo',
#             'objects': http.request.env['na_training_odoo.na_training_odoo'].search([]),
#         })

#     @http.route('/na_training_odoo/na_training_odoo/objects/<model("na_training_odoo.na_training_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('na_training_odoo.object', {
#             'object': obj
#         })
