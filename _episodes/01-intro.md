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

> ## Launching JupyterLab
{: .challenge}

## Setting up the conda environment

> ## Setting up/choosing a conda environment
{: .challenge}

## Testing package installations

> ## Testing your package installs
> `import xarray`
> `import dask`
> `import numba`
> `import numpy`
{: .challenge}


## Downloading the data

### NetCDF recap

### Zarr Data

### Intake Catalogues

> ## Testing you can open the data
> `import xarray`
> `xr.opendataset`
{: .challenge}

