---
title: "Storing and Accessing Data in Parallelism Friendly Formats"
teaching: 50
exercises: 30
questions:
- "How is the performance of data access impacted by bandwidth and latency?"
- "How can we use an object store to store data that is accessible over the internet?"
- "How do we access data in an object store using Xarray?"
objectives:
- "Understand the relative performance of memory, local disks, local networks and the internet."
- "Understand that object stores are a convienient and scalable way to store data to be accessed over the internet."
- "Understand how Zarr files can be structured in an object store friendly way."
- "Apply Xarray to access Zarr files stored in an object store."
keypoints:
- "We can process faster in parallel if we can read or write data in parallel too"
- "Data storage is many times slower than accessing our computer's memory"
- "Object stores are one way to store data that is accessible over the web/http, allows replication of data and can scale to very large quantities of data."
- "Zarr is an object store friendly file format intended for storing large array data."
- "Zarr files are stored in chunks and software such as Xarray can just read the chunks that it needs instead of the whole file."
- "Xarray can be used to read in Zarr files"
---

# Data Access Speeds

## Parallel Filesystems

# Object Stores

# Zarr files

## Zarr and Xarray

> ## Challenge
> the challenge
>> ## Solution
>> the solution
> {: .solution}
{: .challenge}


{% include links.md %}
