# intake-rolling-zarr

[![Build Status](https://travis-ci.com/informatics-lab/intake-rolling-zarr.svg?branch=master)](https://travis-ci.com/informatics-lab/intake-rolling-zarr)

intake-rolling-zarr: Rolling zarr plugin for [Intake](https://github.com/intake/intake)

See [Intake docs](https://intake.readthedocs.io/en/latest/overview.html).

In `intake-rolling-zarr`, there are plugins provided for reading rolling zarr into iris cubes
  - Rolling Zarr

### Installation

The conda install instructions are:

```
conda install -c informaticslab -c intake intake-rolling-zarr
```



import intake_rolling_zarr
data = intake_rolling_zarr.RollingZarrSource('s3://metoffice-aws-earth-zarr/mo-atmospheric-mogreps-uk-prd-air_temperature-at_heights.zarr')
data.read()

cat = intake.open_yaml_file_cat("/Users/theo/repos/intake-rolling-zarr/tests/data/s3.catalog.yaml")


