# -*- coding: utf-8 -*-
import pytest
from intake import open_catalog

@pytest.fixture
def local_prefix_cat():
    path = os.path.dirname(__file__)
    cat = open_catalog(os.path.join(path, 'data', 'local.catalog.yaml'))
    source = cat['mogreps_uk_air_temp'].get()
    assert bool(source.read())