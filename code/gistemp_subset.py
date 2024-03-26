#!/usr/bin/env python

#creates a subset of just the 21st century data for the GISS Surface Temperature Analysis version 4 dataset
#the original dataset can be found at https://data.giss.nasa.gov/pub/gistemp/gistemp1200_GHCNv4_ERSSTv5.nc.gz
#this script was used to prepare the original data, learners do not need to run it.

import xarray as xr
ds = xr.open_dataset("gistemp1200_GHCNv4_ERSSTv5.nc")
ds2 = ds.tempanomaly.isel(time=slice(1440,1730))
print("old dataset:",ds)
print("new dataset:",ds2)
ds2.attrs=ds.attrs
ds2.to_netcdf("gistemp1200-21c.nc")
