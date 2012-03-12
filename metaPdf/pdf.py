#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: pdf
   :platform: Unix, Windows
   :synopsis: The metaPdf implementation.

.. moduleauthor:: Ali Anari <ali@alianari.com>

"""

import os, re

def read_metadata(file_name):
    """This function reads a PDF file and returns its metadata.
    :param file_name: The PDF file name to read.
    :type file_name: str
    :returns: dict -- The returned metadata as a dictionary of properties.

    """

    properties = {}
    with open(str(file), 'rb') as f:
        f.seek(-4096, os.SEEK_END)
        end_block = f.read()
        for p in re.finditer('(?:\/(\w+)\s?\(([^\n\r]*)\)\n?\r?)', end_block, re.S):
            try: properties[p.group(1)] = p.group(2).decode('utf-8')
            except: properties[p.group(1)] = 'ENCRYPTED'
    return properties
