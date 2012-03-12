#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob, re

def read(file):
    properties = {}
    with open(str(file), 'rb') as f:
        f.seek(-4096, os.SEEK_END)
        end_block = f.read()
        for p in re.finditer('(?:\/(\w+)\s?\(([^\n\r]*)\)\n?\r?)', end_block, re.S):
            try: properties[p.group(1)] = p.group(2).decode('utf-8')
            except: properties[p.group(1)] = 'ENCRYPTED'
    return properties
