'''
A simple time-based, columnar data store.
'''

import time
import os

data_in = [
    {
        'path': '/foo',
        'time': 23,
        'status': 200
    },
    {
        'path': '/foo',
        'time': 23,
        'status': 400
    },
    {
        'path': '/foo',
        'time': 23,
        'status': 200
    },
]

FOLDER = './timestore'


def write_file(fname, )


for d in data_in:
    d['timestamp'] = time.monotonic_ns()
