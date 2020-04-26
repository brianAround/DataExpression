from datetime import datetime
from os import path
import pyodbc

servers = {'vpehost': 'east', 'vpwhost': 'west'}

for server in servers:
    env_name = servers[server]

    script_file = "JCCDSelect.sql"

    with open(script_file, 'r') as user_file:
        jccd_query = ''.join(user_file.readlines())


    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=' + server + ';'
                          'Database=Viewpoint;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    jccd_values = {}

    current_date = datetime.now()
    jccd_filename = 'jccd_' + env_name + '_extract_2020_' + str(current_date.month) + '_' + str(current_date.day) \
                    + '_' + str(current_date.hour) + '_' + str(current_date.minute) + '.txt'
    jccd_filename = path.join('Extracts','JCCD', jccd_filename)
    print(jccd_filename)
    column_names = []
    for row in cursor.execute(jccd_query):
        jccd_val = {}
        if len(column_names) == 0:
            column_names = [column[0] for column in cursor.description]
        for idx in range(len(column_names)):
            jccd_val[column_names[idx]] = row[idx]
        jccd_values[row.KeyID] = jccd_val

    with open(jccd_filename, 'w') as write_data:
        write_data.write('\t'.join(column_names))
        write_data.write('\n')
        sorted_keys = sorted([keyid for keyid in jccd_values])
        for keyid in sorted_keys:
            jccd = jccd_values[keyid]
            for key in column_names:
                write_data.write(str(jccd[key]) + '\t')
            write_data.write('\n')

            # write_data.write(str(keyid) + '\t')
            # print('KeyID:', keyid, jccd_values[keyid])

    script_file = "HQMAJCCD.sql"

    with open(script_file, 'r') as user_file:
        hqma_query = ''.join(user_file.readlines())


    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=' + server + ';'
                          'Database=Viewpoint;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    hqma_values = {}

    hqma_filename = 'hqma_' + env_name + '_extract_2020_' + str(current_date.month) + '_' + str(current_date.day) \
                    + '_' + str(current_date.hour) + '_' + str(current_date.minute) + '.txt'
    hqma_filename = path.join('Extracts','HQMA', hqma_filename)
    print(hqma_filename)
    column_names = []
    for row in cursor.execute(hqma_query):
        hqma_val = {}
        if len(column_names) == 0:
            column_names = [column[0] for column in cursor.description]
        for idx in range(len(column_names)):
            hqma_val[column_names[idx]] = row[idx]
        hqma_values[row.AuditID] = hqma_val

    with open(hqma_filename, 'w') as write_data:
        write_data.write('\t'.join(column_names))
        write_data.write('\n')
        sorted_keys = sorted([keyid for keyid in hqma_values])
        for keyid in sorted_keys:
            hqma = hqma_values[keyid]
            for key in column_names:
                write_data.write(str(hqma[key]) + '\t')
            write_data.write('\n')

            # write_data.write(str(keyid) + '\t')
            # print('KeyID:', keyid, jccd_values[keyid])


