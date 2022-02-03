import xmlrpc.client

db = "jense"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

if uid:
    print("Connection Successful")

models = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/object')

to_confrim_ids = models.execute_kw(db, uid, password, 'estate.properties', 'search', [[('name', '=', '1BHK')]])
# print ("\n\nto_confrim_id ::: ", to_confrim_ids)

result = models.execute_kw(db, uid, password, 'estate.properties', 'action_sold', [to_confrim_ids])

# result = models.execute_kw(db, uid, password, 'estate.properties', 'search_read', [[], ['name', 'description', 'state']])

print("\n\nresult is ::: ", result)
