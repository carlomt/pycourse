Python Tutorial 
===============

Material for a short hands-on Python course, based on the course Andrea Dotti (andrea.dotti@gmail.com) gave at the 16th Seminar on Software for Nuclear, Sub-nuclear and Applied Physics, Porto Conte, Alghero (Italy), 26-31 May 2019.

Ths material has been used at
1.  INFN Alghero school 2019
2.  INFN Course at Perugia 2019


## Syllabus
 
The goal of the tutorial is two-fold: introduce some basic concepts to trigger the curiosity of participants on the programming language itself and show some insights on the use of popular data analysis libraries and tools used in the field of data-science.
The first part of the tutorial introduces the general features of the language and highlights the basic constructs (Lectures 1 and 2). The focus of the second part will be on the use of python and its libraries for the analysis and visualization of data (Lectures 3 and 4). 
The course is organized with hands-on interactive exercises. Each topic is presented with interactive examples and simple exercises. Each lecture is concluded by a more challenging exercise. The use of interactive notebooks based on the jupyter technology has become a very popular way of creating interactive data analysis studies. For this reason, starting from the second lecture notebooks will be introduced and the programming exercises will be accomplished in notebooks. Slides will be used only in the first lecture, while starting from the second one the tutorial will use only notebooks.
While a small description of the procedures to install python packages via pip and conda will be discussed the participants will have a pre-installed environment to be used with the Virtual Machine provided by the school. 

 1.	Basic of Python programming language
    a.	Variables, with emphasis on lists and dictionaries
    b.	Control flow
    c.	functions and classes
    d.	Exercise 1: A simple Random Number Generator 
 2.	Simplifying python programming
    a.	Pip/virtualenv & conda
    b.	IPython console
    c.	Jupyter Notebooks
    d.	Exercise 2: Numerical integration - simple pendulum
 3.	Data analysis with Python
    a.	Basic tools for python data handling: Numpy, scipy 
    b.	Plotting with matplotlib
    c.	Pandas DataFrame and data handling
    d.	Exercise 3: Facebook AD Campaign data-analysis
 4.	Exercise 4: Data analysis example
    a.	Iris dataset and logistic regression for classification 
    b.	Hand-written digits recognition with machine learning techniques (optional)

#### Prerequisite
The code is python3, the slides and supporting material is included as python jupyter notebooks.

Anaconda `environment.yml` file can be used to setup an environment with all dependencies.

The code depends on the [Anaconda3 python distribution](https://anaconda.org/).
Install anaconda3, and get the code from this repository.

#### Getting the code
To get the code:

```bash
git clone <thisrepo>
cd <thisrepo>
#Retrieve the reveal.js library used to make the slides. 
#N.B. Using a specific version 3.1
git submodule init
git submodule update
conda env create -f environment.yml
#To be done in each new shell
conda activate pycourse
#Post-installation setup, to do only once
. post-install.sh
```

#### Structure of the project
The project contains the following directories:

 1. `reveal.js`: reveal.js library needed for the slides.
 2. `Slides`: notebooks source code for the lectures slides.
 3. `Notebooks`: Exercises and notebooks.

#### How to create slides
 To look at the slides execute in a shell:

 ```bash
 conda activate pycourse
 jupyter-nbconvert --to slides <path-to-a-slides-notebook> --reveal-prefix=reveal.js --post serve
 ```

 To create a PDF of the slides, add `?print-pdf` to the URL of the served slides, e.g.: `http://localhost:8000/[SLIDES TITLE].slides.html?print-pdf`

#### Exercises
Exercises are in the `Notebooks` directory, solutions are included. Exercise 06 is optional and instead of exercises is a step-by-step tutorial to neural networks.



 