from odoo import models, fields, api

class billing(models.Model):
    _name = 'maint.billing'
    _description = 'billing'
    _rec_name = 'billing_no'


    billing_no = fields.Char(string='Billing number', required=True)
    bill_from_date = fields.Datetime(string='Bill from date', required=True)
    bill_to_date = fields.Datetime(string='Bill to date', required=True)
    customer = fields.Many2one('res.partner', 'customer', readonly=True)

    billing_asset = fields.Many2one('maint.asset', string='Billing_asset', ondelete='cascade')
    tr_view = fields.One2many('maint.chargetransaction', 'ChargerUserID', string='Chargertransaction', ondelete='cascade' )
    #billing_asset_id = fields.One2many('maint.billing', 'billing_asset', ondelete='cascade')

    # def doTest(self):
    #     print("Test")
    #     self.env['maint.chargerTransaction'].sudo().create(
    #         {
    #             "trans_id" :
    #         }
    #     )
        # self.env['maint.billing'].sudo().create({
        #  "billing_no" : "test",
        #     "bill_from_date" : datetime.datetime.now(),
        #     "bill_to_date" : datetime.datetime.now()
        # })

        # rec5 = self.env['maint.billing'].sudo().browse(5)
        # print(rec5)
        # rec5.write({
        #     "billing_no" : str(datetime.datetime.now())
        # })

        # rec5.unlink()


        # recs  = self.env['maint.billing'].sudo().search(
        # [
        #     #( "billing_no", "=", "test")
        # ]
        # )
        # print(recs)
        # if recs is not None and recs.__len__() > 0:
        #     for rec in recs:
        #         print(rec)
        #         #update rec
        #         rec.write({
        #             "bill_to_date" :  rec["bill_to_date"] + datetime.timedelta(days=50)
        #         })





