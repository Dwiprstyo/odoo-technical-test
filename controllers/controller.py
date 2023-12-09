from odoo import http
from odoo.http import request
import json

class ControllerREST(http.Controller):
    
    @http.route([
        '/material',
    ], type='http', auth="none", methods=['GET'],
        csrf=False)
    def getMaterial(self, **post):
        materials = request.env['material.material'].sudo().search([])
        print(materials)
        
        material_data = []
        for material in materials:
            material_data.append({
                'code': material.code,
                'name': material.name,
                'type': material.type,
                'buy_price': material.buy_price,
                'supplier_id': material.supplier_id.name
            })
            
        print(material_data)

        return http.Response(
            status=200,
            content_type='application/json; charset=utf-8',
            response=json.dumps({
                'success': True,
                'data': material_data,
            }),
        )
