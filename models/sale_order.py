# pkm/models/sale_order.py
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    entrega_id = fields.Many2one('pkm.entregas', 'Entrega')
    comentarios = fields.Char('Comentarios')
    oferta_venta = fields.Char('Ofertas de venta')