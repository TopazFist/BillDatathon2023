# BillDatathon2023
In this project, we are matching a set of reciepts to a set of users, each of
whom has a vendor name, total cost, vendor address, and purchase date.

## Project Technical Summary
wjoijfoqwjeoif
wehfkqjwef
qwkqeflkqwef

## Setup
All data is in our Google Drive folder:
https://drive.google.com/drive/u/0/folders/1MzXCKFLMYq2LaYryNc79-pFDkfExN4kb
It was given to us by Bill.com for this specific competition.
- Copy the img and ocr folders into data/original
- Copy Users.csv and test_transactions.csv into data/original as well
- Also be sure to install all libraries in requirements.txt
  - Use the command "pip install -r requirements.txt"

## Running the project
- To clean the data, run scripts/clean_data.py
- Then, to add OCR data from receipts that did not have them given, run scripts/gen_ocr.py
- To create the metrics csv file that is the precursor to generating our matchings, run scripts/create_metrics_dataframe.py
- Then, to find the best parameters for converting these metrics to matchings, run all the cells in lven_vname.ipynb and machine_learning.ipynb
  - The model's accuracy was around 84.2%

## Files
- data/
  - final/                  the directory for processed and final data
  - interim/                the directory cleaned and manipulated data goes into
  - original/               the directory to put the data from drive into
- modules/                  all Python scripts to be imported
  - cvread.py               reads receipts and generated OCRs and confidence intervals
  - lavenshtein.py          contains all functions for lavenshtein-distance related activities
  - rev_helper.py           helps create the array of metrics from the cleaned data
- scripts/                  all Python scripts that the user can run
  - add_confidences.py      an experimental script to determine the OCR confidence in each word
  - clean_data.py           cleaning the Users.csv, test_transactions.csv, and existing OCR data files
  - gen_ocr.py              generates OCR csv files formatted the same way as the ones given, but for receipts without them
  - optimal_matching.py     finds the optimal matching using the final data
- laven_vname.ipynb
- machine_learning.ipynb
- ocr_cv.ipynb
- README.md
- requirements.txt