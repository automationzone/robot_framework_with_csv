import csv
import os

def get_variables(filename):
    variables = {}
    filepath = os.path.dirname(os.path.realpath(__file__))
    filepath = "\\".join(filepath.split("\\")[0:-3]) + "\\Data"
    print(filepath)
    reader = csv.DictReader(open(f'{filepath}\{filename}'))
    for item in reader:
        for each_key in item:
            variables[str(item['testname']) + "." + each_key] = item[each_key]
    return variables



