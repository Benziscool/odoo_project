from odoo import models, fields

class assetType(models.Model):
    _name = 'maint.asset.type'
    _description = 'maint.asset.type'
    _rec_name = 'asset_type'

    asset_type = fields.Char(string='Asset Type', required=True)
    type_description = fields.Char(string='Type Description', required=True)



    #ทีแรกอันนี้เป็น Many2One แต่ error เลยลองสลับเป็น One2Many
    type_id_parent = fields.One2many('maint.asset', 'asset_type_id', ondelete='cascade')  # fields รับจาก maint.asset จาก fields asset type id



