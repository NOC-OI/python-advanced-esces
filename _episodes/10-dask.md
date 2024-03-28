---
title: "Parallelising with Dask"
teaching: 50
exercises: 30
questions:
- "How do we setup and monitor a Dask cluster?"
- "How do we parallelise Python code with Dask?"
- "How do we use Dask with Xarray?"
objectives:
- "Understand how to setup a Dask cluster"
- "Recall how to monitor Dask's performance"
- "Apply Dask to work with Xarray"
- "Apply Dask futures and delayed tasks"
keypoints:
- "Dask is a parallel computing framework for Python"
- "Dask creates a task graph of all the steps in the operation we request"
- "Dask can use your local computer, an HPC cluster, Kubernetes cluster or a remote system over SSH"
- "We can monitor Dask's processing with its dashboard"
- "Xarray can use Dask to parallelise some of its operations"
- "Delayed tasks let us lazily evaluate functions, only causing them to execute when the final result is requested"
- "Futures start a task immediately but return a futures object until computation is completed"
---

# What is Dask?

# Setting up Dask on your computer

## Using the Dask dashboard

# Using Dask with Xarray

lazy loading

# Delayed Tasks

# Futures


> ## Challenge
> the challenge
>> ## Solution
>> the solution
> {: .solution}
{: .challenge}


{% include links.md %}
