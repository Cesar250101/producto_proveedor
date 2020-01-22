# -*- coding: utf-8 -*-
from odoo import http

# class ProductoProveedor(http.Controller):
#     @http.route('/producto_proveedor/producto_proveedor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/producto_proveedor/producto_proveedor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('producto_proveedor.listing', {
#             'root': '/producto_proveedor/producto_proveedor',
#             'objects': http.request.env['producto_proveedor.producto_proveedor'].search([]),
#         })

#     @http.route('/producto_proveedor/producto_proveedor/objects/<model("producto_proveedor.producto_proveedor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('producto_proveedor.object', {
#             'object': obj
#         })