---
title: "Working with data in Xarray"
teaching: 40
exercises: 30
questions:
- "How do I load data with Xarray?"
- "How does Xarray index data?"
- "How do I apply operations to the whole or part of an array?"
- "How do I work with time series data in Xarray?"
- "How do I visualise data from Xarray?"
objectives:
- "Understand the concept of lazy loading and how it helps work with datasets bigger than memory"
- "Understand whole array operations and the performance advantages they bring"
- "Apply Xarray operations to load, manipulate and visualise data"
keypoints:
- "Xarray can load NetCDF files"
- "We can address dimensions by their name"
- "With lazy loading data is only loaded into memory when it is requested"
- "We can apply mathematical operations to the whole (or part) of the array, this is more efficient than using a for loop"
- "We can also apply custom functions to operate on the whole or part of the array"
- "Xarray has many useful built in operations it can perform such as interpolating and downsampling"
- "Broadcasting"
- "time series"
- "visualising"
---

# Introducing Xarray

Xarray is a library for working with multidimensional array data in Python. Many of its ways of working are inspired by Pandas but Xarray is built to work well 
with very large datasets. It is designed to work with popular scientific Python libraries including NumPy and Matplotlib. It is designed to work with arrays that are
larger than the memory of the computer. 

## Loading a NetCDF with Xarray

dataset vs dataarray

dataset based heavily 

dataarray looks like a numpy array, duck typing 

other packages like cuda use these

xr.open_dataset

other engines such as grib, zarr (which we'll look at later)

access data, coords and attrs like netcdf library


# Xarray indexing

ds.tempanomaly or ds['tempanomaly']

to_dataset and to_dataarray to convert



can't use variables with spaces in the dot notation


label space vs index space
index by latitude/longitude/time instead of index value


isel
sel

add a new variable to an array just by using it

data["newvar"] = [ 1,2,3 ]

working with slices

nearest neighbour lookups

# Plotting Xarray data

.plot method

maps/2d images

histograms

facetting?



## Interactive plotting with hvplot

hvplot


> ## Challenge
> the challenge
>> ## Solution
>> the solution
> {: .solution}
{: .challenge}



# Array operations

array mathematical operations

## Computation operations

map/reduce concept

mean, min, max, median, sum etc

## Dealing with Missing data

use where to cut missing values or mask around a country

### Rolling Windows

Moves a window across the array

ds.rolling(time=5, center=True).construct("window")

### Coarse Windows

reduce resolution of data

non-overlapping blocks of an array

ds.coarsen(lat=5,lon=5,boundary="trim")

add .mean().plot()

reshape time into multiple dimensions, e.g. change a monthly data series to a year/month series

### Group by

split-apply-combine pattern, break data into groups, apply a reduction, combine results into a new dimensions

Going from daily to monthly, we have variable length months

groupby_bins 

resampling

isin, checks if value is in a certain range and then assigns a value, e.g. isin(month, [12,1,2])] = "DJF"

## Applying custom functions


## Broadcasting
## Interpolating, downsampling etc

# Working with time series data

date time accessors

da.time
da.time.dt.day
da.time.dt.season

timedate objects?
strftime


# Writing Data



> ## Challenge
> the challenge
>> ## Solution
>> the solution
> {: .solution}
{: .challenge}


{% include links.md %}
