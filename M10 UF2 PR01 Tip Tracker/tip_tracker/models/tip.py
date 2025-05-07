from odoo import models, fields

class Tip(models.Model):
    _name = 'tip.tracker'
    _description = 'Registro de Propinas'
    
    employee_id = fields.Many2one(
        'hr.employee', 
        string='Empleado',
        required=True
    )
    amount = fields.Float(
        'Monto', 
        digits=(12, 2),
        required=True
    )
    date = fields.Date(
        default=fields.Date.context_today
    )
    shift_code = fields.Char(
        string='Código de Turno'
    ) 