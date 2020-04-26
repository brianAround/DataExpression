import json
# import xml.etree.ElementTree as xml
import requests

api_url_base = 'http://irvpvw-ecoint1.prim.com:8080/ecosys/api/restjson/'

headers = {'Content-Type': 'application/json'}

username = 'admin'
password = 'ecosys34'

interface = 'ChangeDetails'


api_url ='{0}{1}/'.format(api_url_base, interface)
response = requests.post(api_url, )

# request_doc = xml.Element(interface + 'Request')



def get_actuals_info():
    # api_url = '{0}account'.format(api_url_base)
    interface = 'CommitmentDetails'
    api_url = '{0}{1}/'.format(api_url_base, interface)

    response = requests.get(api_url, headers=headers, auth=(username, password))



    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return


def get_cost_objects_info():
    # interface = 'WorkingForecastTransactionList'
    # api_url = '{0}account'.format(api_url_base)
    api_url = '{0}{1}/'.format(api_url_base, interface)

    response = requests.get(api_url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return

reslt = get_actuals_info()

for actual_row in reslt['WorkingForecastTransactionList']:
    print(actual_row)
