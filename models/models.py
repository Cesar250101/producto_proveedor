# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductoProveedor(models.Model):
    _inherit = 'product.template'

    proveedor = fields.Char(string="Proveedor", related="seller_ids.name.name",required=False, )
