#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: format_string_scan

:Synopsis:

:Author:
    servilla,costa

:Created:
    5/5/17
"""

import logging
import time
import random

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z', filename='format_string_scan' + '.log',
                    level=logging.INFO)

logger = logging.getLogger('format_string_scan')

import requests
from lxml import etree
import sys


def scan_format_string(black_list=None):

    format_strings = {}
    packages = 0
    packages_with_element = 0
    base_url = 'https://pasta.lternet.edu/package/eml'
    xpath = '//dateTime/formatString'
    scopes = requests.get(url=base_url).text.split('\n')
    for scope in scopes:
        if scope not in black_list:
            identifers = requests.get(url=base_url + '/' + scope).text.split('\n')
            for identifier in identifers:
		time.sleep(random.randint(10,100))
                package_id = scope + '.' + identifier
                print('package_id: {package_id}'.format(package_id=package_id))
                try:
                    url = 'http://pasta.lternet.edu/package/metadata/eml/' + scope + '/' + identifier + '/newest'
                    tree = etree.parse(url)
                    path = tree.findall(xpath)
                    packages += 1
                    if path:
                        packages_with_element += 1
                        for elmt in path:
                            format_string = elmt.text.strip()
                            print('format_string: {package_id} {format_string}'.format(format_string
                                                           =format_string, package_id=package_id))
                            if ',' in list(format_string):
                                format_string = '"' + format_string + '"'
                            if format_string not in format_strings:
                                format_strings[format_string] = 1
                            else:
                                format_strings[format_string] += 1
                except Exception as e:
                    logger.error(e)
    for format_string, value in sorted(format_strings.items()):
        print('output: {str},{n}'.format(str=format_string, n=value))


def main():

    black_list = ('edi','lter-landsat', 'lter-landsat-ledaps', 'ecotrends')
    scan_format_string(black_list=black_list)

    return 0


if __name__ == "__main__":
    main()
