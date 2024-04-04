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

One thing to note is that Xarray has not only plotted the graph, but has also automatically labelled it based on the long names and units for the variables that were in the metadata 
of the dataset. The dates on the X axis are also correctly labelled, whereas many plotting libraries require some extra steps to setup labelling dates correctly.

## Plotting Two Dimensional Data

Xarray isn't just restricted to plotting line graphs, if we select some data that returns latitude and longitude dimensions then the plot function will show a map. 

~~~
dataset['tempanomaly'].sel(time="2000-01-15").plot()
~~~
{: .language-python}

The plot function being called is actually part of the Matplotlib library and we can invoke Matplotlib if we need to modify some of the plotting parameters. For example we might
want to change the colourmap to one which uses grayscale. This can be done by first importing `matplotlib.pyplot` and specifying the `cmap` parameter to `plot()`.

~~~
import matplotlib.pyplot as plt
dataset['tempanomaly'].sel(time="2000-01-15").plot(cmap=plt.cm.Grays)
~~~
{: .language-python}


## Plotting Histograms

Another useful plotting function is to plot a histogram of the data, this could be useful for example to plot the distribution of the temperature anomalies on a given day.
To produce this we call the `plot.hist()` function on a DataArray.

~~~
dataset['tempanomaly'].sel(time="2010-09-15").plot.hist()
~~~
{: .language-python}


## Facetting

Should this be included?


## Interactive Plotting with Hvplot

So far we've used the matplotlib backend to make our visualisations, this produces some nice graphs but they are completely static and changing the view will require us to change the parameters.
Another plotting library we can use is [Hvplot](https://hvplot.holoviz.org/), this library allows interactive plots with zooming, panning and displaying the value the mouse is hovering over.

To use hvplot with xarry we must first import the hvplot library with:

~~~
import hvplot.xarray
~~~
{: .language-python}

then instead of calling `plot()` we can now call `hvplot()`.

~~~
dataset['tempanomaly'].sel(lat=53,lon=-3).hvplot()
~~~
{: .language-python}


> ## Challenge
> Using a slice of the array, plot a transect of the surface temperature anomaly across the Atlantic ocean at 23 degrees North between 70 and 17 degrees West on January 15th 2000 and
> June 15th 2000.
> > ## Solution
> > ~~~
> > dataset['tempanomaly'].sel(time="2000-01-15",lon=slice(-70,-17),lat=23).plot()
> > dataset['tempanomaly'].sel(time="2000-06-15",lon=slice(-70,-17),lat=23).plot()
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}


# Array operations

One of the most powerful features of Xarray is the ability to apply a mathematical operation to part or all of an array. 
Not only is this convienient for us to avoid needing to write one or more for loops to loop over the array applying the operation, it also performs better and can take advantage of 
some optimsations of our processor. Potentially it can also be parallelised to apply multiple operations simulatenously across different parts of the array, we'll see more about this later on.

If for example we want to apply a simple offset to our entire dataset we can add or subtract a constant value to every element by doing:

~~~
dataset_corrected = dataset['tempanomaly'] - 1.0
~~~
{: .language-python}

Just to confirm this worked, let's compare the summaries of both datasets:

~~~
dataset_corrected
dataset['tempanomaly']
~~~
{: .language-python}


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
