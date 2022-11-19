# Final Project ANLP 21-22


This repository contains the final project for the course "Advanced Natural Language Processing" during the winter semester of 2021/2022 at the University of Potsdam by Lara Pfennigschmidt, Laura Riedel and Antonia Schmidt.

It was originally worked on using University of Potsdam's own GitLab platform "Git.UP" transferred to GitHub after the project's conclusion. Therefore, our individual contributions to this project cannot be traced by this repository's commit history.

## Patronizing and Condescending Language Detection

As our project we chose the SemEval 2022 Task 4, Subtask 2, which addresses the topic of Patronizing and Condescending Language (PCL) Detection as a multi-class classification problem. For more details regarding the subtask see the links below.


# Project Subtask Description
https://sites.google.com/view/pcl-detection-semeval2022/

https://competitions.codalab.org/competitions/34344

# Repository Structure

## Reports
Contains our individual project reports we had to hand in in partial requirement of passing the course.

## src
Our source code. 
Note that we cannot include the data set we worked with in this public repository since the data set is provided upon request to the authors only. If you want to use our code in the way we did with the partial dataset provided to us as part of the SemEval Task 2022, please request access directly from the authors via a link provided on their [SemEval GitHub page](https://github.com/Perez-AlmendrosC/dontpatronizeme "dontpatronizeme SemEval 2022").

- data: Contains objects created in our Jupyter Notebooks like embedding matrices, predictions etc. When running `Data Prepocessing` that notebook also creates cleaned data, train/test split etc in this folder.
 	- `data_exploration.Rmd`: Contains some initial data exploration using R.
	- This is also where we kept Pérez-Almendros et al.'s (2020) Don't Patronize Me! dataset (in a folder titled "dontpatronizeme_v1.4"), made available to us after contacting the authors. For reasons explained above it is not included here.

- dontpatronizeme: Contains code files directly taken from https://github.com/Perez-AlmendrosC/dontpatronizeme as well as files where we modified their code to fit our needs better.
- `0. Data Preprocessing`: Jupyter Notebook containing first corpus explorations and our data preprocessing.
- `1. Logistic Regression`: Jupyter Notebook containing our Logistic Regression approach to PCL classification.
- `2. Bi-LSTM`: Jupyter Notebook containing our BiLSTM approach to PCL classification.
- `3. Random Baseline`: Jupyter Notebook containing a random baseline to compare to our results.
- `4. Analysis`: Jupyter Notebook containing some analysis of the data and the prediction results
- `embedding_functions`: Python file containing outsourced "helper" functions for dealing with GoogleNews embeddings.

# Requirements/what we have been working with
- scikit-learn, version 1.0.2
- scikit-multilearn, version 0.2.0
- pandas, version 1.4.1
- numpy, version 1.22.3
- nltk, version 3.7
- torch, version 1.10.1
- graphviz, version 2.50.0
- gensim, version 4.1.2
- matplotlib, version 3.5.0
- tensorflow (with keras), version 2.8.0
- python, version 3.8.3 or higher
- R, version 4.0.2
