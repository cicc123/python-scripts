from mk_db_file import loadDbase,storeDbase
db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'TOm TOM'
storeDbase(db)
