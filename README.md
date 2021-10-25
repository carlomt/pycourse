Python Tutorial 
===============

[Site](http://www.roma1.infn.it/~mancinit/?action=3Teaching/Python)

Material for a short hands-on Python course, based on the course Andrea Dotti (andrea.dotti@gmail.com) gave at the 16th Seminar on Software for Nuclear, Sub-nuclear and Applied Physics, Porto Conte, Alghero (Italy), 26-31 May 2019.

Ths material has been used at
1.  INFN Alghero school 2019
2.  INFN Course at Perugia 2019
3.  INFN Course at Perugia 2021


## Syllabus

The goal of the tutorial is two-fold: introduce some basic concepts to trigger the curiosity of participants on the programming language itself and show some insights on the use of popular data analysis libraries and tools used in the field of data-science. 
After a brief introduction, the focus of the tutorial will be on the use of python and its libraries for the analysis and visualization of data. 
The course is organized with hands-on interactive exercises. Each topic is presented with interactive examples and simple exercises. The use of interactive notebooks based on the jupyter technology has become a very popular way of creating interactive data analysis studies. For this reason jupyter will be introduced and the programming exercises will be accomplished in notebooks. 
While a small description of the procedures to install python packages via pip and conda will be discussed the participants will have a pre-installed environment to be used with the Virtual Machine provided by the school. 

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
conda env create -f environment.yml
#To be done in each new shell
conda activate pycourse
#Post-installation setup, to do only once
. post-install.sh
#Use .\post-install.ps1 on Windows 10 PowerShell
```

#### Structure of the project
The project contains the following directories:

 1. `Slides`: notebooks source code for the lectures slides.
 2. `Notebooks`: Exercises and notebooks.

#### How to create slides
 To look at the slides execute in a shell:

 ```bash
 conda activate pycourse
 jupyter-nbconvert --to slides <path-to-a-slides-notebook> --post serve
 ```

 To create a PDF of the slides, add `?print-pdf` to the URL of the served slides, e.g.: `http://localhost:8000/[SLIDES TITLE].slides.html?print-pdf`

#### Exercises
Exercises are in the `Notebooks` directory, solutions are included. Exercise 06 is optional and instead of exercises is a step-by-step tutorial to neural networks.

 1. `00_notebook_tutorial.ipynb` Tutorial for the use of jupyter notebooks
 2. 


 
