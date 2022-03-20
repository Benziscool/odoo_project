from odoo import models, fields

class BillingLine(models.Model):
    _name = 'maint.billing.line'
    _description = 'maint.billing.line'
    _rec_name = 'transid'

    billing_ids = fields.Char(string='billing_ids', required=True)
    transid = fields.Many2one('maint.chargetransaction', string='Trans_id', ondelete='cascade') #สลับจากเดิม Many2one เป็น One2many