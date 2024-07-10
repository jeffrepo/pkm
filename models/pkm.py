from odoo import models, fields

class PkmEntregas(models.Model):
	_name = 'pkm.entregas'
	_description = 'Entregas'

	name = fields.Char('Nombre')