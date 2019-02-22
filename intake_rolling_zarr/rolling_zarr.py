# -*- coding: utf-8 -*-
from . import __version__
from intake.source.base import DataSource
from .rolling_store import OffSetS3Map
import xarray


def maybe_to_iris(ds):
    if len(ds.data_vars) == 1:
        return ds[list(ds.data_vars)[0]].to_iris()

    return ds


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
        if not url.startswith('s3://'):
            raise ValueError('url must be a valid s3 url starting s3://')
        url = url[len('s3://'):]
        self._url = url
        self._temp_chunk_path = temp_chunk_path
        self._ds = None

    def read(self):
        print(self._url)
        if not self._ds:
            store = OffSetS3Map(root=self._url,
                                temp_chunk_path=self._temp_chunk_path,
                                check=False)
            self._ds = xarray.open_zarr(store)
        return maybe_to_iris(self._ds)

    def to_dask(self):
        self._get_schema()
        return self._dataframe

    def _close(self):
        self._dataframe = None
        self._ds = None
