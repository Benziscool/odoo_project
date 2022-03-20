import datetime

from odoo import models, fields, api

class locationtype(models.Model):
    _name = 'maint.location.type'
    _description = 'maint.location.type'
    _rec_name = 'type_description'
    #ใส่ชื่อฟิลด์ที่ต้องการเอาไปโชว์ใน _rec_name

    location_type = fields.Char(string='location type', required=True)
    type_description = fields.Char(string='description', required=True)

    def doTest(self):
        print("Test")
        # self.env['maint.billing'].sudo().create({
        #  "billing_no" : "test",
        #     "bill_from_date" : datetime.datetime.now(),
        #     "bill_to_date" : datetime.datetime.now()
        # })

        rec5 = self.env['maint.billing'].sudo().browse(5)
        print(rec5)
        rec5.write({
            "billing_no" : str(datetime.datetime.now())
        })

        rec5.unlink()

        recs  = self.env['maint.billing'].sudo().search(
        [
            #( "billing_no", "=", "test")
        ]
        )
        print(recs)
        if recs is not None and recs.__len__() > 0:
            for rec in recs:
                print(rec)
                #update rec
                rec.write({
                    "bill_to_date" :  rec["bill_to_date"] + datetime.timedelta(days=50)
                })
