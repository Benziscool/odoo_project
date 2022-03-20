# -*- coding: utf-8 -*-
# from odoo import http


# class EzMaint(http.Controller):
#     @http.route('/ez_maint/ez_maint/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ez_maint/ez_maint/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ez_maint.listing', {
#             'root': '/ez_maint/ez_maint',
#             'objects': http.request.env['ez_maint.ez_maint'].search([]),
#         })

#     @http.route('/ez_maint/ez_maint/objects/<model("ez_maint.ez_maint"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ez_maint.object', {
#             'object': obj
#         })
