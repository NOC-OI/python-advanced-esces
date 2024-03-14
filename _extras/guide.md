---
title: "Instructor Notes"
---

The instructor notes should provide additional discussion useful to instructors,
but not appropriate for inclusion in the main lessons. The following structure
provides a consistent way for instructors to both prepare for a workshop and
quickly find necessary information during a workshop.

Please remember not to overload on details, and to keep the comments here positive!

## Lesson motivation and learning objectives

Aimed at people who have:

* Completed an introductory Python Carpentries course
and
* Spent at least one year developing Python Code
* Completed an intermediate course such as the Intermediate Software Development or Intermediate ESCES Course

Are familiar with the following concepts:

* Writing Python scripts/notebooks
* Variable handling
* Importing, calling and writing functions
* Loops
* Working with data in arrays of lists, Pandas dataframes or Numpy arrays
* Using slicing operations on Python datastructures
* Using plotting libraries such as matplotlib

Learners are NOT required to be familiar with the following:

* Object Oriented Programming
* Functional Programming

They will want to:

* Use Python to work with large datasets (those approaching or exceeding the size of their computer's memory)
* Apply parallelisation techniques to process larger data and to do so faster
* Better structure their data and use appropriate file formats for large datasets
* Understand how to analyse the efficiency of their code and improve it
* Work with a wide range of Python libraries
* Work with time series data
* Work with geospatial data
* Visaulise data
* Run programs on HPC or Cloud systems
* Use GPUs


Possible things to include:
* Web APIs
* Advanced/Intermediate Git
* Iterators and Generators
* Apply machine learning



## Lesson design

### Dataset Selection
* A time series 2D or 3D geospatial dataset with at least one parameter.
* For example sea surface temperature or air temperature at 1 or 1/4 degree resolution?
* In NetCDF format + Zarr formats 
* Subset of it as a set of images for the GNU parallel exercises (possibly numpy/numba too)
* Ideally we want at least a few GB of data, need to host it somewhere or stick it on a shared filesystem if everyone uses the same HPC

### Introduction (10 minutes teaching, 20 minutes exercises)
* What are the common challenges of working with big data? Too big for memory, takes too long to process in serial, difficult to store/access, dependent on lots of libraries.

#### Setting up our environment
* Getting connected to our target system
* Setting up conda/mamba envrionments

### Dataset Parallelism with GNU Parallel (10 minutes teaching, 15 minutes exercise)
* What is GNU parallel
* Example applying an operation to a multi-file dataset in parallel

### Working with data in Xarray (40 minutes teaching, 30 minutes exercises)
* Explain about NetCDF
* How to load data with Xarray
* Lazy loading and evaluation
* Applying operations to whole datasets
* Visualising Xarray data

### Plotting Geospatial data with Cartopy (30 minutes teaching, 20 minutes exercises)
* Dealing with projections
* Adding grid lines, country outlines etc
* Working with Xarray data

### Storing and Accessing Data in Parallelism Friendly formats (20 minutes teaching, 30 minutes exercises)
* Zarr files and working with them in Xarray
* Object stores, storing data in the cloud
* Importance of chunking, file ordering
* Parallel filesystem implications
* Intake Catalogues

### Parallel Processing With Numpy and Numba (50 minutes teaching, 30 minutes exercises)
* Profiling
  * time/timeit magic in Jupyter
  * Using lineprofiler at command line and in Jupyter
* Numpy whole array operations
* Parallelising with Numba ufuncs

### Parallelising with Dask (50 minutes teaching, 30 minutes exercises)
* Using Dask on your own computer
* Using Dask on a remote computer(s)
* Launching the Dask dashboard
* Dask with Xarray (and Pandas or Numpy?)
* Delayed tasks
* Futures

### Parallelising Machine Learning with Dask (40 minutes teaching, 35 minutes exercises)
* Scikit learn intro, how to use train and fit functions.
* Train a classifier or estimator using Dask
* Train with a dataset too big for RAM

### Using GPUs (35 minutes teaching, 25 minutes exercises)
* Why use GPUs?
* Use GPUs with Numba
* GPU accelerated libraries (cuDF for Pandas, cuPY for Numpy, cuML for scikit learn)

### things not covered that might need to be:
* Something more biology friendly, some ecological observation data? Perhaps in the geospatial visualisation section?
* Standard python advanced topics, lambdas, generators, OOP (can probably sneak lambdas in, in a few places)
* Using Pandas dataframes, we jump straight to Xarray, is this a problem?


## Technical tips and tricks


## Common problems

