# -*- coding: utf-8 -*-
from . import __version__
from intake.source.base import DataSource, Schema

import json
import dask.dataframe as dd
from datetime import datetime, timedelta
import s3fs
from .rolling_store import OffSetS3Map
import xarray

class RollingZarrSource(DataSource):
    """Common behaviours for plugins in this repo"""
    name = 'rolling_zarr'
    version = __version__
    container = 'xarray'
    partition_access = True

    def __init__(self, url=None, temp_chunk_path=None, metadata=None):
        """
        Parameters
        ----------
        path : str
            The S3 url to the  which contains the manifest files.
        """
        self._path = path
        self._temp_chunk_path = temp_chunk_path
        


        # if self._manifest_date == 'latest':
        #     self._manifest_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        # self._s3_prefix = s3_prefix
        # self._urlpath = '{prefix}{manifest_bucket}/{source_bucket}/{config_id}/{date}/manifest.json'.format(
        #     prefix=self._s3_prefix,
        #     manifest_bucket=self._manifest_bucket,
        #     source_bucket=self._source_bucket,
        #     config_id=self._config_id,
        #     date=self._manifest_date)
        # self._extract_key_regex = extract_key_regex
        # if self._extract_key_regex is not None:
        #     self._extract_key_regex = r'%s' % extract_key_regex
        # self._s3_manifest_kwargs = s3_manifest_kwargs or {}
        # self._dataframe = None



    def read(self):
         store = OffSetS3Map(root=self._path, temp_chunk_path=self._temp_chunk_path, check=False)
         return xarray.open_zarr(store)


    def _get_partition(self, i):
        self._get_schema()
        return self._dataframe.get_partition(i).compute()

    def read(self):
        self._get_schema()
        return self._dataframe.compute()

    def to_dask(self):
        self._get_schema()
        return self._dataframe

    def _close(self):
        self._dataframe = None
