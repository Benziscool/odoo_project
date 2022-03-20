from odoo import models, fields

class assetCategory(models.Model):
    _name = 'maint.asset.category'
    _description = 'maint.asset.category'
    _rec_name = 'location_id'

    asset_category = fields.Char(string='Asset Category', required=True)
    category_description = fields.Char(string='description', required=True)

    asset_ids = fields.One2many('maint.asset', 'asset_category_id', string='asset_id', ondelete='cascade')

    location_type_id = fields.Many2one('maint.location.type', ondelete='cascade')
    #location_id = fields.Many2one('maint.location', ondelete='cascade')

    location_id = fields.Many2one('maint.location', string='location_id', ondelete='cascade')

