# -*- coding: utf-8 -*-

import sys
import os
import re
import json

from bs4 import BeautifulSoup

def parse(filename):
    result   = {}
    basename = os.path.basename(filename).replace('+', ' ')

    with open(filename) as f:
        data = f.read()
        soup = BeautifulSoup(data, 'html.parser')

        for table in soup.select('table'):
            for tr in table.select('tr'):
                td = tr.select('td')

                if len(td) == 1:
                    title = re.sub(r'^[0-9]+\.', '', td[0].text).strip()

                    result['Manufacturer'] = basename
                    result['Model']        = title[len(basename) + 3:]
                else:
                    key   = td[0].text.strip()
                    value = td[1].text.strip()

                    if key == 'Version':
                        result['Model']    = result['Model'] + ' ' + value
                    elif key == 'Method':
                        result['Protocol'] = value
                    elif key == 'User ID':
                        result['Username'] = value
                    elif key == 'Password':
                        result['Password'] = value

    return result

if __name__ == '__main__':
    result = []
    for a in sys.argv[1:]:
        tmp = parse(a)
        result.append(tmp)

    with open('data2.json', 'wb') as f:
        f.write(json.dumps(result))

                        


