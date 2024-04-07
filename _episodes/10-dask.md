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

![Dask dashboard graph view](../fig/Dask-Task-Graph.png)

![Dask dashboard task view](../fig/Dask-Status.png)

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

# Dask Arrays

Dask has its own type of arrays, these behave much like Numpy (and Xarray) arrays, but they can be split into a number of chunks. Any processing operations can work in parallel across
these chunks. Data can also be loaded "lazily" into Dask Arrays, this means it is only loaded from disk when it is accessed. This can give us the illusion of loading a dataset that
is larger than our memory.

## Creating a Dask Array

Dask arrays can be created from existing from other array formats including NumPy arrays, Python lists and PandasDataFrames. 
We can also initalise a new array as a Dask Array from the start, Dask copies the `zeros`, `ones` and `random` functions from NumPy which initalise an array as all zeros, ones or as 
random numbers. For example to create a 10000x10000 array of random numbers we can use:

~~~
import dask.array as da
x = da.random.random((10000, 10000), chunks=(1000, 1000))
x
~~~
{: .language-python}

Dask arrays support common Numpy operations including slicing, arithmetic whole array operations, reduction functions such as `mean` and `sum`, transposing and reshaping.

~~~
y = da.ones((10000,10000), chunks = (1000, 1000))
z = x + y
z
~~~
{: .language-python}

In the above example we added the x and y arrays together, but when we display the result we just get an array getitem in response instead of an actual value. This is because Dask
hasn't actually computed the result yet. Dask works by building up a dependency graph of all the operations we're performing, but doesn't compute anything until we call the `compute`
function on the final result. Let's go ahead and call `compute` on the `z` object, if we monitor the Dask Dashboard we should see some activity.

~~~
result = z.compute()
result
~~~
{: .language-python}

The new variable result will now contain the result of the computation and will be of the type `numpy.ndarray`.

~~~
type(result)
~~~
{: .language-python}

> ## Compare Dask and Numpy Performance
> Compare the performance of the following code using Numpy and Dask functions. Use the %%time magic in the cells to find out the execution time. Ensure you only time the core computation
> and not the Dask cluster setup or library imports, this means you'll have to write this code into multiple cells.
> Dask version (note you'll need to do the Dask client setup first):
> ~~~
> import dask.array as da
> x = da.random.random((20000,20000), chunks=(1000,1000))
> x_mean = x.mean()
> x_mean.compute()
> ~~~
> {: .language-python}
> Numpy version:
> ~~~
> import numpy as np
> npx = np.random.random((20000,20000))
> npx_mean = npx.mean()
> ~~~
> {: .language-python}
> Which went faster overall? Why do you think you got the result you did? Try making the dataset a little larger, going much beyond 25000x25000 might use too much memory.
> Try running the `top` command in a terminal while your notebook is running, look at the CPU % when running the Numpy and Dask versions and compare them. Try changing the 
> number of Dask threads and see what effect this has on the CPU %.
{: .challenge}



### Troubleshooting Dask

Sometimes Dask can jam up and stop executing tasks. If this happens try the following:

- Shutdown the client and restart it.
- Shutdown the kernel of your notebook and rerun the notebook.


## Using Dask with Xarray

lazy loading


# Low Level computation with Dask

## Delayed Tasks

## Futures

# Using the JASMIN Dask gateway

JASMIN offers a Dask Gateway service which can submit Dask jobs to a special queue on the Lotus cluster.

~~~
import dask_gateway
import dask
gw = dask_gateway.Gateway("https://dask-gateway.jasmin.ac.uk", auth="jupyterhub")

options = gw.cluster_options()
options.worker_cores = 1
options.scheduler_cores = 1
options.worker_setup='source /apps/jasmin/jaspy/mambaforge_envs/jaspy3.10/mf-22.11.1-4/bin/activate ~/.conda/envs/esces'

clusters = gw.list_clusters()
if not clusters:
    cluster = gw.new_cluster(options, shutdown_on_close=False)
else:
    cluster = gw.connect(clusters[0].name)

client = cluster.get_client()
~~~
{: .language-python}


~~~
# Create at least one worker, and allow your cluster to scale to 15.
# The max JASMIN allows is 16, but one of these is used as the scheduler.
cluster.adapt(minimum=1, maximum=15)
~~~
{: .language-python}

~~~
ssh -J <jasminusername>@login2.jasmin.ac.uk sci6
squeue -p dask
~~~
{: .language-bash}


> ## Challenge
> the challenge
>> ## Solution
>> the solution
> {: .solution}
{: .challenge}


{% include links.md %}
