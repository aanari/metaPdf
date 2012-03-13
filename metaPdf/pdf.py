#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: pdf
   :platform: Unix, Windows
   :synopsis: The metaPdf implementation.

.. moduleauthor:: Ali Anari <ali@alianari.com>

"""


import os, re


metadata_regex = re.compile('(?:\/(\w+)\s?\(([^\n\r]*)\)\n?\r?)', re.S)
metadata_offset = 2048
start_header = 10240 / metadata_offset

totalcount = 0

def end_metadata(f, depth, multiplier):

    """This is a helper method called by read_metadata.

    """

    lastindex = depth/multiplier
    f.seek((depth * -metadata_offset), os.SEEK_END)
    for i in range(1, lastindex):
        properties = dict((p.group(1), p.group(2)) for p in metadata_regex.finditer(f.read(multiplier * metadata_offset)))
        if properties: break
    return properties

def read_metadata(file_name):

    """This function reads a PDF file and returns its metadata.
    :param file_name: The PDF file name to read.
    :type file_name: str
    :returns: dict -- The returned metadata as a dictionary of properties.

    """

    with open(str(file_name), 'rb') as f:

        # Scan the last 2048 bytes, the most
        # frequent metadata density block
        f.seek(-metadata_offset, os.SEEK_END)
        properties = dict((p.group(1), p.group(2)) for p in metadata_regex.finditer(f.read(metadata_offset)))
        if properties:
            return properties

        # Scan forward from the last 200 * 2048
        # bytes, the next high density region
        properties = end_metadata(f, 200, 10)
        if properties:
            return properties

        # Investigate the header at 5 * 2048
        f.seek(0)
        properties = find_metadata(f.read(start_header * metadata_offset), properties)
        if properties:
            return properties

        # Do a fast scan through the last 1000 * 2048
        properties = end_metadata(f, 800, 50)
        if properties:
            return properties

        # Last ditch attempt, scan entire file
        f.seek(start_header)
        while True:
            properties = dict((p.group(1), p.group(2)) for p in metadata_regex.finditer(f.read(metadata_offset*4)))
            if properties:
                return properties

    return {}
