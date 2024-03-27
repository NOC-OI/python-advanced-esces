---
title: "Introduction"
teaching: 15
exercises: 10
questions:
- "How can I use Python to work with large datasets?"
- "How do I connect to a high performance computing system to run my code?"
objectives:
- "To have the lesson conda environment installed and running."
- "To be able to launch a JupyterLab instance with the lesson's data and code present."
- "To be aware of the key libraries used in this lesson (Xarray, Numba, Dask, Intake)."
keypoints:
- "Python can scale to using large datasets with the Xarray library."
- "Python can parallelise computation with Dask or Numba."
- "NetCDF format is useful for large data structures as it is self-documenting and handles multiple dimensions."
- "Zarr format is useful for cloud storage as it chunks data so we don't need to transfer the whole file."
- "Intake catalogues make dealing with multifile datasets easier."
---

## How do we scale Python to work with big data?

Python is an increasingly popular choice for working with big data. In enviromental sciences we often encounter data that is bigger
than our computer's memory and/or that is too big to process with our desktop or laptop computers.

> ## What are your needs?
> 1. In the etherpad write a sentence about what kind of data you work with and how big that data is.
> 2. Describe the problems you have working with data that is too big for your desktop or laptop computer to handle.
> 3. List any tools, libraries and computing systems you use or have used to overcome this.
{: .challenge}

### The tools we'll look at in this lesson

In this lesson we will look at a few tools to help you work with big data and to process your data more efficiently and by using parallel processing, these will include:

* GNU Parallel
* Numpy
* Numba
* Xarray
* Dask
* Zarr
* Intake

## Connecting to a JupyterLab/notebook service

We will be using the Notebook service on the JASMIN system for this workshop. This will open a Jupyter notebook in your web browser, 
from this you can type in Python code and it will run on the JASMIN system. JASMIN is the UK's data analysis facility for environmental science 
and co-locates both data storage and data processing facilities. It will also be possible to run much of the code in this workshop on your own 
computer, but some of the larger examples will probably exceed the memory and processing power of your computer.

> ## Launching JupyterLab
> In your browser connect to [https://notebooks.jasmin.ac.uk](https://notebooks.jasmin.ac.uk).
> If you have an existing JASMIN account then login with your normal username and password.
> There is a two factor authentication on the notebook service that will email you a code, enter this code and you will be connected to the Notebook service.
> If you do not have a JASMIN account then please use one of the training accounts provided.
{: .challenge}

## Download examples and set up the Mamba environment

To ensure we have all the packages needed for this workshop we'll need to create a new mamba environment (mamba is a conda compatible package manger but is much faster than conda).
This is defined by a YAML file that is downloaded alongside the course materials.

> ## Download the course material
> Open a terminal and type:
> ~~~
> curl https://github.com/NOC-OI/python-advanced-esces/raw/gh-pages/data/data.tgz > data.tgz
> tar xvf data.tgz
> ~~~
> {: .language-bash}
{: .challenge}


> ## Setting up/choosing a Mamba environment
> From the terminal run the following:
> ~~~
> mamba env create -f esces-env.yml -n esces
> mamba run -n esces python -m ipykernel install --user --name ESCES
> ~~~
> After about one minute if you click on the blue plus icon near the top left or the file menu and "New Launcher" option you should see a notebook option called ESCES.
> This will use the Mamba environment we just created and will have access to all the packages we need.
> {: .language-bash}
{: .challenge}

## Testing package installations

> ## Testing your package installs
> Run the following code to check that you can import all the packages we'll be using and that they are the correct versions. 
> The !parallel runs the parallel command from the command line from within a Jupyter notebook cell. This will not work if you use stanard Python.
> ~~~
> import xarray
> import dask
> import numba
> import numpy
> import cartopy
> import intake
> import zarr
> import netCDF4
> print("Xarray version:", xarray.__version__)
> print("Dask version:", dask.__version__)
> print("Numpy version:", numpy.__version__)
> print("Numba version:", numba.__version__)
> print("Cartopy version:", cartopy.__version__)
> print("Intake version:", intake.__version__)
> print("Zarr version:", zarr.__version__)
> print("netCDF4 version:", netCDF4.__version__)
> !parallel
> ~~~
> {: .language-python}
> > ## Solution
> > You should see version numbers that are equal or greater than the following:
> > ~~~
> > Xarray version: 2024.2.0
> > Dask version: 2024.3.1
> > Numpy version: 1.26.4
> > Numba version: 0.59.0
> > Cartopy version: 0.22.0
> > Intake version: 2.0.4
> > Zarr version: 2.17.1
> > netCDF4 version: 1.6.5
> > GNU parallel 20230522
> > Copyright (C) 2007-2023 Ole Tange, http://ole.tange.dk and Free Software
> > Foundation, Inc.
> > License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
> > This is free software: you are free to change and redistribute it.
> > GNU parallel comes with no warranty.
> >
> > Web site: https://www.gnu.org/software/parallel
> >
> > When using programs that use GNU Parallel to process data for publication
> > please cite as described in 'parallel --citation'.
> > ~~~
> > {: .output}
{: .challenge}

## About the example data

There is a small example dataset included in the download above. This is a Surface Temperature Analysis from the [Goddard Institute for Space Studies at NASA](https://data.giss.nasa.gov/gistemp/). 
It contains a monthly surface temperatures on a 2x2 degree grid from across the earth from 1880 to 2023. The data is stored in a NetCDF file. We will be using a subset of the data that runs from 2000 to 2023.

### About NetCDF files

NetCDF files are suited for storing array data

They are:

 - Self Describing, there is a metadata describing the whole dataset, the variables within it and their units.
 - Widely supported, there are libraries to read netCDF in most programming languages and lots of tools to manipulate them.
 - Python has a NetCDF4 library that can work with them, the Xarray library also works with NetCDF.
 - Efficient, can store data in binary formats instead of ASCII data as CSV would.
 - Able to contain multiple variables
 - Contains three types of data:
    - Variables: the actual data.
    - Dimensions: the dimensions on which the variables exist, for example latitude, longitude and time.
    - Attributes: Information about the dataset, for example who created it and when.

### Exploring the GISS Temp Dataset

#### Load and get an overview of the dataset

~~~
import netCDF4
dataset = netCDF4.Dataset("gistemp1200-21c.nc")
print(dataset)
~~~
{: .language-python}



#### Get the list of attributes
~~~
dataset.ncattrs()
['title', 'institution', 'source', 'Conventions', 'history']
print(dataset.title)
'GISTEMP Surface Temperature Analysis'
~~~
{: .language-python}

#### Get the list of variables
~~~
print(dataset.variables)
~~~
{: .language-python}

#### Get the list of dimensions
~~~
print(dataset.dimensions)
~~~
{: .language-python}


#### Read some data from out dataset
The dataset values can be read from `dataset.variables['variablename']`, it will have a subarray that contains the data following the dimensions specified. 
In our dataset we can see that the tempanomaly variable has the shape `int16 tempanomaly(time, lat, lon)`. 
This means that time will be the first index, latitude the second and longitude the third. We can get the first timestep for the upper left coordinate by using:
~~~
print(dataset.variables['tempanomaly'][0,0,0])
~~~
{: .language-python}
One thing to note here is that our dataset's y coordinates are backwards to most maps (following a computer graphics convention where 0 is the upper left coordinate, not the lower left or centre). 
Therefore requesting `[0,0,0]` means the southern most and western most coordinate at the first timestep.


#### Read some NetCDF data
> ## Challenge
> There are 90 elements to the latitude dimension, one every two degrees and 180 in the longitude dimension, also with one every two degrees. 
> To translate from a real latitude and longitude to an index we'll need to divide the longitude by two and add 90 to the longitude. 
> For the latitude we'll need to flip the coordinate's sign by subtracting it from zero and then divide by two and add 45. 
> In Python this can be expressed as the following, we'll also want to ensure the result is an integer by wrapping the whole calculation in `int()`:
> ~~~
> latitude_index = int(((0 - latitude) / 2) + 45)
> longitude_index = int((longitude / 2) + 90)
> ~~~
> {: .language-python}
> For the time dimension, each element represents one month starting from January 2000, so for example element 12 will be January 2001 (0-11 are January to December 2000).
> For example 54 degrees north (latitude) and 2 degrees west will translate to the array index 72, 46
> Write some code to get the temperature anomaly for January 2020 in Oslo, Norway (approximately 60 North, 10 East)
> > ## Solution
> > ~~~
> > latitude = 60
> > longitude = 10
> > latitude_index = int(((0 - latitude) / 2) + 45)
> > longitude_index = int((longitude / 2) + 90)
> > time_index = 20 * 12   #we want jan 2020, dataset starts at jan 2000 and has monthly entries 
> > print(dataset.variables['tempanomaly'][time_index,latitude_index,longitude_index])
> > ~~~
> > {: .language-python}
> > ~~~
> > 0.39999998
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}


{% include links.md %}