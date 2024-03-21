---
title: "Dataset Parallelism"
teaching: 15
exercises: 10
questions:
- "How do we apply the same command to every file in a dataset?"
objectives:
- "Use GNU Parallel to apply the same command to every file in a dataset"
keypoints:
- "The curl or wget commands can be used to download datasets."
- "GNU Parallel can apply the same command to every file in a dataset"
- "GNU Parallel works on the command line and doesn't require Python, but it can run multiple copies of a Python script"
- "It is often the simplest way to apply parallelism"
- "It requires a problem that works independently across a set of files or a range of parameters"
- "Without invoking a more complex job scheduler, GNU Parallel only works on a single computer"
- "By default GNU Parallel will use every CPU core available to it"
---

# Dataset Parallelism with GNU Parallel

## Installing parallel


## Obtaining our example dataset

Use wget or curl
gunzip

> ## Download the dataset yourself
> wget https://
>> ## Solution
>> the solution
> {: .solution}
{: .challenge}



## Basic use of GNU Parallel

In shell we could use

```
for file in $(ls) ; do
    echo $file
done
```
{: .bash}

GNU parallel version
`parallel echo {1} ::: $(ls)`


Python example
```
for file in $(ls *.nc) ; do
    python myscript.py $file
done
```
{: .bash}

Parallel version
`parallel python myscript.py {1} ::: $(ls *.nc)`

## Working with multiple arguments

`parallel python myscript-2.py {1} {1}.out ::: $(ls *.nc)`

## Using a list of files stored in a file

`ls *.nc | grep "^ABC" > files.txt`
`parallel python myscript-2.py {1} {1}.out :::: files.txt`

## More complex arguments

`parallel echo "hello {1} {2}" ::: 1 2 3 ::: a b c`

For example, if you had a list of netcdf files in files.txt, and you wanted to perform an analysis of two of the varibles, you could use:

`parallel process.py --variable={1} {2} ::: temp sal :::: files.txt`


#### Pairing arguments


`parallel echo "hello {1} {2}" ::: 1 2 3 :::+ a b c`

```
hello world 1 a
hello world 2 b
hello world 3 c
```
{: .output}

## Job Control and Logging

--max-procs argument

--joblog 


> ## Use GNU Parallel yourself
> the challenge
>> ## Solution
>> the solution
> {: .solution}
{: .challenge}


{% include links.md %}
