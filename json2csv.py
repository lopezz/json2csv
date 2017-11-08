"""
Takes a json file and returns a csv with some of the
json attributes
"""

import json
import csv

from collections import OrderedDict

def json2csv():
    '''
    no docstring
    '''
    header = ['index', 'shortname', 'name', 'unicode', 'unicode_encoded', 'aliases', 'image']
    columns = ['shortname', 'name', 'unicode']
    with open('emojione.json', 'r') as j:
        emojis = json.load(j, object_pairs_hook=OrderedDict)
    with open('emojis.csv', 'w') as output:
        emojis_csv = csv.writer(output, delimiter=',', lineterminator='\n',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        emojis_csv.writerow(header)
        for i, ele in enumerate(emojis):
            row = [str(i+1)]
            row += [emojis[ele][x] for x in columns
                    if x not in ('unicode_encoded', 'aliases', 'image')]
            unicodes = emojis[ele]['unicode'].split('-')
            # print(unicodes)
            unicode_encoded = []
            for code in unicodes:
                zeros = '0' * (8 - len(code))
                unicode_str = '\\U'+zeros+code
                unicode_encoded.append(str(unicode_str.encode(), 'unicode-escape'))
            # print(unicode_encoded)
            row.append(' '.join(unicode_encoded))
            row.append(' '.join(emojis[ele]['aliases']))
            row.append('!https://cdn.jsdelivr.net/emojione/assets/png/%s.png?v=2.2.7!'
                       % emojis[ele]['unicode'])
            emojis_csv.writerow(row)

json2csv()
