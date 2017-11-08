"""
Takes a json file and returns a csv with some of the
json attributes
"""

import json
import csv

def json2csv():
    '''
    no docstring
    '''
    columns = ['shortname', 'name', 'unicode', 'unicode_encoded', 'aliases']
    with open('emojione.json', 'r') as j:
        j_data = j.read()
        emojis = json.loads(j_data)
    print(type(emojis))
    with open('emojis.csv', 'w') as output:
        emojis_csv = csv.writer(output, delimiter=',', lineterminator='\n',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        emojis_csv.writerow(columns)
        for i in emojis:
            row = [emojis[i][x] for x in columns if x not in ('unicode_encoded','aliases')]
            unicodes = emojis[i]['unicode'].split('-')
            # print(unicodes)
            unicode_encoded = []
            for code in unicodes:
                zeros = '0' * (8 - len(code))
                unicode_encoded.append(str(bytes('\\U'+zeros + code, 'utf-8'), 'unicode-escape'))
            # print(unicode_encoded)
            row.append(' '.join(unicode_encoded))
            row.append(' '.join(emojis[i]['aliases']))
            emojis_csv.writerow(row)
            #output.write(','.join(row)+'\n')

json2csv()


# with open('emojis.csv', 'w') as f
