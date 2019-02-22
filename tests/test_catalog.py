# -*- coding: utf-8 -*-
import pytest
from intake import open_catalog
import os

def test_open_and_read_private_s3():
    path = os.path.dirname(__file__)
    cat = open_catalog(os.path.join(path, 'data', 's3.catalog.yaml'))
    source = cat['mogreps_uk_air_temp'].get()
    assert bool(source.read())