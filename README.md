Summarizing Abstract For Automatic Title Assignment (SAATA)
======================================

MIDS w266 project
------------
    Waqas Ali
    Dickey Woo
    Marshal Ma

Project Organization
------------
## Overview
In this project, we are exploring different techniques to summarize the abstracts of academic papers into titles automatically. We explore methods including fine tuning state-of-the-art sequence-to-sequence models like T5, PEGASUS, BART. In addition, we explore techniques in replacing academic terms with unknown tokens in text pre-processing as well as pointer-generator neural network structures to improve the performance. 

## Guideline for Reading
You can find the following information in this repository:

Data folder: The data we used are stored under the data folder. The "raw" folder contains the data from Kaggle and the "interim" folder contains the training and test split of the original data.

Notebooks folder:
* BART: Contains th BART model training and scoring notebooks
* PEGASUS: Contains the PEGASUS model training and scoring notebooks
* PointerGenerator: Contains the pointer generator training and scoring notebooks
* T5: Contains the T5 training and scoring notebooks
* TextRank: Contains the TextRank notebooks

References folder: The main papers cited in the final report

Reports folder: Copies of reports

SRC folder: Contains the script we used to create training and testing data

Models folder: The models folder is empty - they are all trained and store on Google Drive due to its size and are not pushed into this repo