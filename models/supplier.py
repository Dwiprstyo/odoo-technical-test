from odoo import models, fields, api

class MaterialType(models.Model):
    _name = 'material.supplier'
    _description = 'Supplier'
    _rec_name = 'name'
    
    name = fields.Char('name')