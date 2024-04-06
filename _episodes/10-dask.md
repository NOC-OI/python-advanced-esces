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

Dask is a Distributed processing library for Python. It enables parallel processing of Python code across multiple cores on the same computer or across multiple computers. It can be 
used behind the scenes by Xarray with minimal modification to code. JASMIN users can make use of a Dask gateway that allows their Dask code submitted from the Jupyter notebook interface
to run on the Lotus HPC cluster. Dask has two broad categories of features, high level data structures which behave in a similar way to common Python data structures but with the 
ability to perform operations in parallel and low level task scheduling to run any Python code in parallel. 

# Setting up Dask on your computer

Dask should already be installed in your Conda/Mamba environment. Dask refers to the system it runs the computation on as a Dask "cluster", although the "cluster" can just be running
on your local computer (or the JASMIN notebook server). Later on we'll look at using a remote cluster running on a different computer, but for now let's create one on our own computer.

~~~
from dask.distributed import Client, progress
client = Client(processes=False, threads_per_worker=4,
                n_workers=1, memory_limit='2GB')
client
~~~
{: .language-python}

The code above will create a local Dask cluster with one worker and 4 threads for each worker and a limit of 2GB of memory. Displaying the `client` object will tell us all about the
cluster.


## Using the Dask dashboard

In the information about the Dask cluster is a link to a Dashboard webpage. From the Dashboard we can monitor our Dask cluster and see how busy it is, view a graph of task dependencies,
 memory usage and the status of the Dask workers. This can be really useful when checking if our Dask cluster is behaving correctly and working out how optimially our code is making
use of Dask's parallelism.

![Dask dashboard graph view](fig/Dask-Task-Graph.png)

![Dask dashboard task view](fig/Dask-Status.png)

### Using the Dask dashboard on JASMIN

Note that if you are using the JASMIN notebook service, the link to the dashboard won't work as the port it runs on isn't open to connections from the internet. 

~~~
ssh-keygen #MAKE SURE YOU SET A PASSPHRASE
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
ssh -R 8787:localhost:8787 login2.jasmin.ac.uk
~~~
{: .language-bash}

Port 8787 might not be the port your Dask cluster is using, make sure the first 8787 is the number your Dask cluster is running on.
If anybody else is doing this then port 8787 on login2 might be in use, change the second 8787 to something else to match. Now connect an SSH tunnel from your computer
to Jasmin login2 and forward port 8787 back to your computer, if you changed 8787 to something else in the previous step then use the same number here in both cases.

~~~
ssh -L 8787:localhost:8787 login2.jasmin.ac.uk
~~~
{: .language-bash}

Open your web browser to http://127.0.0.1:8787 and you will see your Dask cluster page. Note that you have just exposed this to anybody else with JASMIN access and there is no password
on it. 

# High Level Dask datastructures 

## Using Dask with Xarray

lazy loading


# Low Level computation with Dask

## Delayed Tasks

## Futures


> ## Challenge
> the challenge
>> ## Solution
>> the solution
> {: .solution}
{: .challenge}


{% include links.md %}
