import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



# Use a service account
cred = credentials.Certificate('firebase_api.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
# result = db.cllection('charger-charge-historians').document('doc-id').stream()
# print(result)


#print(db)
tb = "charger-charge-historians"
histories_ref = db.collection(tb)
histories = histories_ref.stream()
# #print(histories)
#
# tc = "all-trans"
# all_ref = db.collection(tc)
# all = db.collection(tc).stream()
for history in histories:
  #print(history.to_dict())
   path1 = tb + "/" + history.to_dict()["doc-id"] + "/all-trans"
   #path2 = path1 + "/" + all.to_dict()["status"]
   #doc_ref = path1 + "/" + path1.to_dict()["backendTransID"] +"/ALF0000000001_1625425761856"
   doc_ref = db.collection(path1).document('ALF0000000001_1625425761856').get().to_dict()
   print(doc_ref.get('chargerUserID'))
   print(doc_ref)
   # print(doc_ref.get('chargerUserID'))
   #print(doc_ref())




  # data_ref = db.collection(path1).document('ALF0000000001_1625425761856').get()
      #print(f"path2[status] {path2['status']}")





# tb = "chargers"
# trans = db.collection(tb).stream()
# for tran in trans:
#   #print(f"charger => {tran.id} => {tran.to_dict()} " )
#   data = tran.to_dict()
#   print(f"data[chargerStatus] {data['charger_status']}")

