import os.path


def sort_flat_file(filename, has_header=True, key_column=None, delimiter='\t'):
    print(filename)
    lines = []
    column_line = ''
    column_names = []
    keyid_idx = -1 if has_header else int(key_column)
    full_data = {}
    with open(filename, 'r') as file_input:
        lines = file_input.readlines()
        for line in lines:
            if len(column_names) == 0 and has_header:
                column_line = line
                column_names = [column.strip('\n') for column in line.split('\t') if column != '\n']
                print(column_names)
                keyid_idx = column_names.index(key_column)
            else:
                values = [value.strip('\n') for value in line.split('\t') if value != '\n']
                keyid = values[keyid_idx]
                full_data[keyid] = line

    keys_sorted = sorted([key for key in full_data])

    with open(filename, 'w') as file_output:
        file_output.write(column_line)
        for key in keys_sorted:
            file_output.write(full_data[key])

sort_flat_file('Extracts/RevCalc/EastRevCalcActualsVersion2.txt', key_column='ExternalKey')

