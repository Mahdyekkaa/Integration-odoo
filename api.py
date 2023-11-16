import xmlrpc.client

url = 'http://localhost:8069'
db = 'odoo16'

data = {
    'params': {
        'login': 'admin',
        'password': 'admin',
        'db': 'odoo16'
    }
}

username = 'admin'

password = 'admin'
# Authentication

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

if uid:
    print("authentication done")
else:
    print("authentication field ")

# Search method

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
partner = models.execute_kw(db, uid, password, 'doctor_doctor', 'search', [[]])

# Read method

partner2 = models.execute_kw(db, uid, password, 'doctor_doctor', 'read', [partner],
                              {'fields': ['name', 'age']})

# Search & Read method

partner3 = models.execute_kw(db, uid, password, 'doctor_doctor', 'search_read', [],
                             {'fields': ['name', 'age'], 'limit': 5})

# Create method

vlas = {
    'name': "mahdy",
    'age': "56",
    'gender': "male"
}
Create_id = models.execute_kw(db, uid, password, 'doctor_doctor', 'create', [vlas])

# Update method

partner_search = models.execute_kw(db, uid, password, 'res.partner', 'search',
                                   [[['email', '=', 'mahdy_rady@gmail.com']]])


ko = models.execute_kw(db, uid, password, 'res.partner', 'write',
                  [partner_search, {'mobile': "01205282026"}])

# Delete method

partner_search_unlink = models.execute_kw(db, uid, password, 'doctor_doctor', 'search',
                                    [[['name', '=', 'mahdy']]])

models.execute_kw(db, uid, password, 'doctor_doctor', 'unlink', [partner_search_unlink])
