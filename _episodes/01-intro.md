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

* Datasets bigger than memory
* Processing requirements beyond our own computers

> ## What are your needs?
> 1. In the etherpad write a sentence about what kind of data you work with and how big that data is.
> 2. Describe the problems you have working with data that is too big for your desktop or laptop computer to handle.
> 3. List any tools, libraries and computing systems you use or have used to overcome this.
{: .challenge}

### The tools we'll look at in this lesson

* GNU Parallel
* Numpy and Numba
* Xarray
* Dask
* Zarr


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
> {: .bash}
{: .challenge}


> ## Setting up/choosing a Mamba environment
> From the terminal run the following:
> ~~~
> mamba env create -f esces-env.yml -n esces
> mamba run -n esces python -m ipykernel install --user --name ESCES
> ~~~
> After about one minute if you click on the blue plus icon near the top left or the file menu and "New Launcher" option you should see a notebook option called ESCES.
> This will use the Mamba environment we just created and will have access to all the packages we need.
> {: .bash}
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
> print("Xarray version:", xarray.__version__)
> print("Dask version:", dask.__version__)
> print("Numpy version:", numpy.__version__)
> print("Numba version:", numba.__version__)
> print("Cartopy version:", cartopy.__version__)
> print("Intake version:", intake.__version__)
> print("Zarr version:", zarr.__version__)
> !parallel
> ~~~
> {: .python}
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

### NetCDF recap

### Zarr Data

### Intake Catalogues

> ## Testing you can open the data
> `import xarray`
> `xr.opendataset`
{: .challenge}

{% include links.md %}