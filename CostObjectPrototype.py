import json
import requests

# api_url_base = 'http://irvpvw-ecoint1.prim.com:8080/ecosys/api/restjson/'
api_url_base = 'http://lfstvw-ecotest.prim.com:8080/ecosys/api/restjson/'

headers = {'Content-Type': 'application/json'}

username = 'admin'
password = 'ecosys34'

# interface = 'CostObjects'



def get_commitment_details():
    interface = 'API_Viewpoint_Commitment_Details'
    # api_url = '{0}account'.format(api_url_base)
    api_url = '{0}{1}/'.format(api_url_base, interface)

    response = requests.get(api_url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['WorkingForecastTransactionList']
    else:
        return

def get_commitment_details_rev():
    interface = 'API_Viewpoint_Commitment_Details_Rev'
    # api_url = '{0}account'.format(api_url_base)
    api_url = '{0}{1}/'.format(api_url_base, interface)

    response = requests.get(api_url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['WorkingForecastTransactionList']
    else:
        return

def get_change_details():
    interface = 'API_Viewpoint_Change_Line_Items'
    # api_url = '{0}account'.format(api_url_base)
    api_url = '{0}{1}/'.format(api_url_base, interface)

    response = requests.get(api_url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['WorkingForecastTransactionList']
    else:
        return

def get_revenue_ls():
    interface = 'API_Viewpoint_Revenue_Lump_Sum'
    # api_url = '{0}account'.format(api_url_base)
    api_url = '{0}{1}/'.format(api_url_base, interface)

    response = requests.get(api_url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['WorkingForecastTransactionList']
    else:
        return

def get_revenue_actuals():
    interface = 'API_ActualsRevenue/?StartDate=1/1/2018&EndDate=2/7/2020'
    api_url = '{0}{1}'.format(api_url_base, interface)

    response = requests.get(api_url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['ActualTransactionList']
    else:
        return


def get_commitment_headers():
    interface = 'API_Viewpoint_Commitments'
    # api_url = '{0}account'.format(api_url_base)
    api_url = '{0}{1}/'.format(api_url_base, interface)

    response = requests.get(api_url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['TaskList']
    else:
        return

def get_cost_objects_info():
    interface = 'CostObjects'
    # api_url = '{0}account'.format(api_url_base)
    api_url = '{0}{1}/'.format(api_url_base, interface)

    response = requests.get(api_url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['CostObjectList']
    else:
        return

reslt = get_revenue_actuals()
columns = []

with open('Actuals_Revenue_NoProject.txt', 'w') as outfile:
    for row in reslt:
        if len(columns) == 0:
            columns = []
            for key in row:
                columns.append(key)
            output = '\t'.join(columns)
            print(output)
            outfile.write(output + '\n')
        if row['Project'] == '':
            column_values = []
            for key in columns:
                column_values.append(row[key])
            output = '\t'.join(column_values)
            print(output)
            outfile.write(output + '\n')
