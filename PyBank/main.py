import os
import csv

csvpath=os.path.join("Desktop","budget_date2.csv)

with open (csvpath, newline="") as csvfile:
                     csvreader=csv.reader(csvfile,delimiter=",")
                     
