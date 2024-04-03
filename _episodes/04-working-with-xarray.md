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
with very large datasets. It is designed to work with popular scientific Python libraries including NumPy and Matplotlib. It is also designed to work with arrays that are
larger than the memory of the computer. 

## Datasets and DataArrays

Xarray has two core data types, the DataArray and Dataset. A DataArray is a multidimensional array of data, similar to a NumPy array but with named dimensions. 
Xarray takes advantage of a Python feature called "Duck Typing", where objects can be treated as another type if they implement the same methods (functions). This allows for
Numpy to treat an Xarray DataArray as a Numpy array and vice-versa. A Dataset object contains multiple DataArrays and is what we can load NetCDF files into, it will also include metadata about the dataset. 


### Opening a NetCDF Dataset

We can open a NetCDF file as an Xarray Dataset using the open_dataset function.

~~~
import xarray as xr
dataset = xr.open_dataset("gistemp1200-21c.nc")
~~~
{: .language-python}

In a similar way to the NetCDF library, we can explore the dataset by just giving the variable name:

~~~
dataset
~~~
{: .language-python}

Or we can explore the attributes with the `.attrs` variable, dimensions with `.dims` and variables with `.variables`.

~~~
print(dataset.attrs)
print(dataset.dims)
print(dataset.variables)
~~~
{: .language-python}

The `open_dataset` function isn't restricuted to just opening NetCDF files and can also be used with other formats such as GRIB and Zarr. We will look at using Zarr files later on.

## Accessing data variables

To access an indivdual variable we can use an array style notation:

~~~
print(dataset['tempanomaly']
~~~
{: .language-python}

Or a single dimension of the variable with:

~~~
print(dataset['tempanomaly']['time']
~~~
{: .langauge-python}

Individual elements of the time data can be accessed with an additional dimension:

~~~
print(dataset['tempanomaly']['time'][0]
~~~
{: .language-python}

Xarray has another way to access dimensions, instead of putting the name inside array style square brackets we can just put . followed by the varaible name, for example:

~~~
print(dataset.tempanomaly)


Xarray also has the `sel` and `isel` functions for accessing a variable based on name or index. For example we can use:

~~~
dataset['tempanomaly']['time'].sel(time="2000-01-15")
~~~
{: .language-python}

or

~~~
dataset['tempanomaly']['time'].isel(time=0)
~~~
{: .language-python}

Slicing can be used on Xarray arrays too, for example to get the first year of temperature data from our dataset we could use

~~~
dataset['tempanomaly'][:12]
~~~
{: .language-python}


or

~~~
dataset.tempanomaly[:12]
~~~
{: .language-python}


An alternative way to do this using the sel function with the slice option:
~~~
dataset['tempanomaly'].sel(time=slice("2000-01-15","2000-12-15"))
~~~
{: .language-python}


One possible reason to using the sel method instead of the array based indexing is that sel supports variables with spaces in their names, while the dot notation doesn't.
Although all these different styles can be used interchangbly, for the purpose of providing readable code it is helpful to be consistent and choose one style throughout our program.

### Nearest Neighbour Lookups

We have seen that we can lookup data for a specific date using the sel function, but these dates have to match one which is held within the dataset. For example if we try to lookup
data for January 1st 2000 then we'll get an error since there is no entry for this date.

~~~
dataset['tempanomaly'].sel(time='2000-01-01')
~~~
{: .language-python}

But Xarray has an option to specify the nearest neighbour using the option `method='nearest'`.

~~~
dataset['tempanomaly'].sel(time='2000-01-01',method='nearest')
~~~
{: .language-python}

Note that this has actually selected the data for 2000-01-15, the nearest available to what we requested.


# Plotting Xarray data

We can plot some data for a single location, across all times in the dataset by using the following:

~~~
dataset['tempanomaly'].sel(lat=53, lon=-3).plot()
~~~
{: .language-python}


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
