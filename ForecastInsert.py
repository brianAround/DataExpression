import json
import pyodbc

users = {}

import_file, table_name = "RevenueProjection.json", "EcoSysRevenueForecast"
# import_file, table_name = "ContingencyItems.json", "EcoSysContingency"
# import_file, table_name = "CostForecast.json", "EcoSysCostForecast"

with open(import_file, 'r') as user_file:
    users = json.load(user_file)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=btrtvw-vptest3;'
                      'Database=Viewpoint;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

for forecast in users['TransactionSummaryList']:
    vpuser = '-'
    # print(i['LoginName'])
    columns = ['[' + value + ']' for value in forecast.keys()]
    # cursor.execute("SELECT VPUserName from DDUP where lower(VPUserName) = 'prim\\" + i['LoginName'] + "'")
    insert_template = "INSERT INTO " + table_name + " (" + ','.join(columns) + ") " \
                      "VALUES (" + ','.join([forecast[key]if key in ('Hours','Amount') else "'" + forecast[key] + "'"  for key in forecast]) + ")"
    print(insert_template)

    with conn.cursor() as cursor:
        cursor.execute(insert_template)

    #break


"""  { 
    "ViewpointID": "EAST",
    "JCCo": "12",
    "Job": "43368",
    "ProjectionCode": "0199- 5000-  000-34",
    "ProjectionDate": "03/25/2020 07:09:19",
    "PhaseGroup": "12",
    "Phase": "0199- 5000-  000",
    "CostType": "34",
    "Description": "EcoSys Projection Import",
    "Hours": "38130",
    "Amount": "3922530",
    "User": "jmurty"
  },"""