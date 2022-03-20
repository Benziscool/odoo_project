import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from odoo import models, fields

class ChargeTransaction(models.Model):
    _name = 'maint.chargetransaction'
    _description = 'maint.chargetransaction'
    _rec_name = 'ChargerUserID'

    trans_id = fields.One2many('maint.billing.line', 'transid', ondelete='cascade')
    startAt = fields.Integer(string='startAt', required=True)
    stopAt = fields.Integer(string='stopAt', required=True)
    ChargerUserID = fields.Char(string='ChargerUserID', required=True)
    ChargerLocID = fields.Char(string='ChargerLocID', required=True)
    ChargerID = fields.Char(string='ChargerID', required=True)
    connectorID = fields.Char(string='connectorID', required=True)
    identityKey = fields.Char(string='identityKey', required=True)
    startCmd = fields.Char(string='startCmd', required=True)
    chargeType = fields.Char(string='chargeType', required=True)
    lockedAt = fields.Integer(string='lockedAt', required=True)
    unlockedAt = fields.Integer(string='unlockedAt', required=True)
    vehicle = fields.Char(string='vehicle', required=True)
    chargedBy = fields.Char(string='chargedBy', required=True)
    backendTransID = fields.Char(string='backendTransID', required=True)

    chargeRateKW = fields.Integer(string='chargeRateKW', required=True)
    chargeRatePerMin = fields.Integer(string='chargeRatePerMin', required=True)

    totalChargeTime = fields.Float(string='totalChargeTime', required=True) #ให้เก็บเป็น float ได้เลยไหม
    totalChargeKW = fields.Integer(string='totalChargeKW', required=True)

    startMeter = fields.Integer(string='startMeter', required=True)
    stopMeter = fields.Integer(string='stopMeter', required=True)

    payeeRef = fields.Char(string='payee', required=True)
    payRef = fields.Char(string='payRef', required=True)
    paidStatus = fields.Char(string='paidStatus', required=True)
    paymentSource = fields.Char(string='paymentSource', required=True)
    lineTransRef = fields.Char(string='lineTransRef', required=True)

    prepaidCost = fields.Float(string='prepaidCost', required=True)
    prepaidKey = fields.Char(string='prepaidKey', required=True)
    chargeCurrency = fields.Char(string='chargeCurrency', required=True)

#test firebase start
    cred = credentials.Certificate('firebase_api.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    tb = "charger-charge-historians"
    histories_ref = db.collection(tb)
    histories = histories_ref.stream()

    for history in histories:
        # print(history.to_dict())
        path1 = tb + "/" + history.to_dict()["doc-id"] + "/all-trans"
        # path2 = path1 + "/" + all.to_dict()["status"]
        # doc_ref = path1 + "/" + path1.to_dict()["backendTransID"] +"/ALF0000000001_1625425761856"
        doc_ref = db.collection(path1).document('ALF0000000001_1625425761856').get().to_dict()
        print(doc_ref.get('chargerUserID'))
        print(doc_ref)
