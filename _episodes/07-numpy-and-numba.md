---
title: "Parallelisation with Numpy and Numba"
teaching: 50
exercises: 30
questions:
- "How can we measure the performance of our code?"
- "How can we improve performance by using Numpy array operations instead of loops?"
- "How can we improve performance by using Numba?"
objectives:
- "Apply profiling to measure the performance of code."
- "Understand the benefits of using Numpy array operations instead of loops."
- "Remember that single instruction, multiple data instrcutions can speed up certain operations that have been optimised for their use."
- "Understand that Numba is using Just-in-time compilation and vectorisation extensions."
- "Understand when to use ufuncs and gufuncs to write functions that are compatible with Numba."
keypoints:
- "We can measure how long a Jupyter cell takes to run with %%time or %%timeit magics."
- "We can use a profiler to measure how long each line of code in a function takes."
- "We should measure performance before attemping to optimise code and target our optimisations at the things which take longest."
- "Numpy can perform operations to whole arrays, this will perform faster than using for loops."
- "Numba can replace some Numpy operations with just in time compilation that is even faster."
- "One way numba achieves higher performance is to use vectorisation extensions of some GPUs that process multiple pieces of data in one instruction."
- "Numba ufuncs and gufuncs let use write arbitary functions for Numba to use."
---

# Profiling

# Numpy whole array operations

# Numba

## What is Numba and how does it work?

### Single Instruction, Multiple Data (SIMD)

## Ufuncs and Gufuncs




> ## Challenge
> the challenge
>> ## Solution
>> the solution
> {: .solution}
{: .challenge}


{% include links.md %}
