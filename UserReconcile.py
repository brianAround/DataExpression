import json
import pyodbc

users = {}

with open("Viewpoint_Usernames.json", 'r') as user_file:
    users = json.load(user_file)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=vpwhost;'
                      'Database=Viewpoint;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

for i in users['UserList']:
    vpuser = '-'
    # print(i['LoginName'])
    cursor.execute("SELECT VPUserName from DDUP where lower(VPUserName) = 'prim\\" + i['LoginName'] + "'")
    for row in cursor:
        vpuser = row[0]
    print(i['LoginName'] + '\t' + vpuser)

