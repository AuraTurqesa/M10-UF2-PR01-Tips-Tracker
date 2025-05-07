from odoo import models, fields, api

class TipTracker(models.Model):
    _name = 'tip.tracker'
    _description = 'Gestor de Propinas'
    _order = 'date desc, id desc'

    employee_id = fields.Many2one('hr.employee', string='Empleado', required=True)
    amount = fields.Float(string='Cantidad', required=True)
    date = fields.Date(string='Fecha', required=True, default=fields.Date.context_today)
    shift_code = fields.Char(string='Código Turno', required=True)
    
    # New fields
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('paid', 'Pagado'),
        ('cancelled', 'Cancelado')
    ], string='Estado', default='draft', required=True)
    
    shift_type = fields.Selection([
        ('morning', 'Mañana'),
        ('afternoon', 'Tarde'),
        ('night', 'Noche')
    ], string='Tipo de Turno', required=True)
    
    service_type = fields.Selection([
        ('table', 'Servicio de Mesa'),
        ('bar', 'Servicio de Barra'),
        ('delivery', 'Delivery'),
        ('other', 'Otro')
    ], string='Tipo de Servicio', required=True)
    
    payment_method = fields.Selection([
        ('cash', 'Efectivo'),
        ('card', 'Tarjeta'),
        ('mixed', 'Mixto')
    ], string='Método de Pago', required=True)
    
    notes = fields.Text(string='Notas')
    bill_amount = fields.Float(string='Importe Factura')
    tip_percentage = fields.Float(string='Porcentaje Propina', compute='_compute_tip_percentage', store=True)
    
    @api.depends('amount', 'bill_amount')
    def _compute_tip_percentage(self):
        for record in self:
            if record.bill_amount:
                record.tip_percentage = (record.amount / record.bill_amount) * 100
            else:
                record.tip_percentage = 0.0

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_pay(self):
        self.write({'state': 'paid'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'}) 