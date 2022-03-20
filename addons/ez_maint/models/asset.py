from odoo import models, fields

class asset(models.Model):
    _name = 'maint.asset'
    _description = 'maint.asset'
    _rec_name = 'asset_type_id'


    asset_num = fields.Char(string='asset_num', required=True)
    asset_description = fields.Char(string='asset_description', required=True)
    serialnum = fields.Char(string='serial', required=True)
    install_date = fields.Datetime(string='Install Date', required=True)
    expire_date = fields.Datetime(string='expire Date', required=True)
    initial_cost = fields.Integer(string='Initial cost', required=True)
    addition_info = fields.Char(string='Addition Info', required=True)

    asset_category_id = fields.Many2one('maint.asset.category', string='Asset Category ID', ondelete='cascade') # ลองสลับจาก one2many เป็น many2one

    asset_type_id = fields.Many2one('maint.asset.type', string='asset_type_id', ondelete='cascade')
    vendor = fields.Many2one('res.partner', string='Vendor', readonly=True)
    owner = fields.Many2one('res.partner', string='Owner', readonly=True)
    billing_asset_id = fields.One2many('maint.billing', 'billing_asset', ondelete='cascade')  # parent_asset(link to another asset)
    location_id = fields.Many2one('maint.location', ondelete='cascade')

