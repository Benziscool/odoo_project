from odoo import models, fields

class Location(models.Model):
    _name = 'maint.location'
    _description = 'main.location'

    name = fields.Char(string='Description', required=True)
    location = fields.Char(string='Location', required=True)
    lat = fields.Integer(string='Lat', required=True)
    lng = fields.Integer(string='Lng', required=True)

    location_type_id = fields.Many2one('maint.location.type')

    # owner = fields.Many2one('res.partner', string='Owner', readonly=True)
    # owner_id = fields.Many2one('res.partner', string='owner_id', readonly=True)

    owner_id = fields.One2many('maint.asset', 'owner', readonly=True)
    owner = fields.Many2one('res.partner', string='Owner', readonly=True)

    #หนึ่งโลเคชั่นมีเจ้าของได้คนเดียว
    #วิ่งจากลูกไปหาแม่

    # def create(self):
    #     val = {
    #         'name': self.name,
    #         'notes': 'Created frome the wizard'
    #     }
    #     self.env['Location'].create(val)


