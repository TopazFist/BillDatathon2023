# BillDatathon2023
In this project, we are matching a set of reciepts to a set of users, each of
whom have a vendor name, total cost, vendor address, and purchase date.

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
- Then, to find the best parameters for converting these metrics to matchings, run scripts/optimal_matching.py
  - The script will also run these parameters on the testing dataset and show the accuracy
  - The model's accuracy was around 84.2%
