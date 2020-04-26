import os.path


filename = 'Extracts/JCCD/jccd_east_extract_2020_4_25_7_53.txt'
lines = []
column_names = []
key_column = 'KeyID'
full_data = {}
with open(filename, 'r') as file_input:
    lines = file_input.readlines()
    for line in lines:
        if len(column_names) == 0:
            column_names = [column for column in line.split('\t') if column != '\n']
        else:
            values = [value for value in line.split('\t') if value != '\n']


filename2 = 'Extracts/JCCD/jccd_east_extract_2020_4_25_7_53_sorted.txt'



