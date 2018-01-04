#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import json
import requests
import itertools

from bs4 import BeautifulSoup

def parse(filename):
    result = {}

    with open(filename, 'r') as f:
        data = f.read()
        soup = BeautifulSoup(data, 'html.parser')

        for tr in soup.select('tbody tr'):
            td = tr.select('td')
            if len(td) != 5:
                print 'Invalid rows', tr.text
                continue
            else:
                result['Manufacturer'] = td[0].text
                result['Model'] = td[1].text
                result['Protocol'] = td[2].text
                result['Username'] = td[3].text
                result['Password'] = td[4].text

    return result


if __name__ == '__main__':
    result = []
    for a in sys.argv[1:]:
        tmp = parse(a)
        result.append(tmp)

    with open('data.json', 'wb') as f:
        f.write(json.dumps(result))
