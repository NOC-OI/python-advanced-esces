---
title: "GPUs"
teaching: 35
exercises: 25
questions:
- "What are GPUs and how do we access them?"
- "How can we use a GPU with Numba?"
- "How can we use a GPU in Pandas, Numpy or SciKit Learn?"
objectives:
- "Understand what the difference between a GPU and CPU is and the performance implications"
- "Apply Numba to use a GPU"
- "Understand that there are GPU enabled replacements for many popular Python libraries"
- "Recall that NVIDIA GPUs can be programmed in CUDA, but this is a very low level operation"
keypoints:
- "GPUs are Graphics Processing Units, they have large numbers of very simple processing cores and are suited to some parallel tasks like machine learning and array operations"
- "Many laptops and desktops won't have very powerful GPUs, instead we'll want to use HPC or Cloud systems to access a GPU."
- "Google's Colab provides free access to GPUs with a Jupyter notebooks interface."
- "Numba can use GPUs with minor modifications to the code."
- "NVIDIA have drop in replacements for Pandas, Numpy and SciKit learn that are GPU accelerated."
---

# What are GPUs and why should we use them?

- GPUs are Graphics Processing Units, they have large numbers of very simple processing cores and are suited to some parallel tasks like machine learning and array operations
- GPUs used to have to be programmed using specialised languages/libraries such as Cuda (NVIDIA proprietary) or OpenCL (cross platform and open source). 
- These are very low level systems that require the programmer to worry about things like moving data to/from GPU memory. 
- Today many higher level libraries can use GPUs reducing our need to learn Cuda or OpenCL.

## How can you access a GPU if your PC doesn't have one

- Many laptops and desktops won't have very powerful GPUs, instead we'll want to use HPC or Cloud systems to access a GPU.
- Google Colab (https://colab.research.google.com) offers a Jupyter notebook interface with GPUs for free, but the GPUs aren't very powerful.

# Using GPUs

## Using GPUs with Numba
- Numba can use GPUs with minor modifications to the code.
- The key thing we need to do is use the `@cuda.jit` decorator.
- The GPU has its own memory and we need to copy data to/from this.


## GPU replacements for popular libraries
- NVIDIA have drop in replacements for Pandas, Numpy and SciKit learn that are GPU accelerated. The replacemnt for Numpy is known as Cupy.

The following will calculate the mean of 100,000,000 random numbers using Cupy.

~~~
import cupy as cp
a = cp.random.random(100_000_000)
%time cp.mean(a)
~~~
{: .language-python}

For comparison let's do the same using numpy as see how long it takes.

~~~
import numpy as np
a = np.random.random(100_000_000)
%time np.mean(a)
~~~
{: .language-python}



> ## Challenge
> the challenge
>> ## Solution
>> the solution
> {: .solution}
{: .challenge}


{% include links.md %}