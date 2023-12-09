from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material.material'
    _description = 'Material'
    
    code = fields.Char('code', required=True)
    name = fields.Char('name', required=True)
    type = fields.Selection([
        ('Fabric', 'Fabric'),
        ('Jeans', 'Jeans'),
        ('Cotton','Cotton')
    ], string='type',required=True)
    buy_price = fields.Float('buy_price',required=True)
    supplier_id = fields.Many2one('material.supplier', string='supplier',required=True) 
        
    @api.model
    def create(self, values):
        res = super(Material, self).create(values)
        if values['buy_price'] < 100:
            raise ValidationError("Tidak boleh kurang dari 100")