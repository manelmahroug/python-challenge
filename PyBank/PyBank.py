
# coding: utf-8

# In[84]:


import os
import csv
import sys

csv_path1 = os.path.join("..","Desktop", "budget_data_1.csv") #creating a path across operating systems

# budget 1
print("Financial Analysis")
print("----------------------------------------")
totalMonths(csv_path)
totalRevenue(csv_path)
avgChange(csv_path)
maxChange(csv_path)
minChange(csv_path)
    



# In[82]:


# total number of months 

def totalMonths(csv_path):
    with open (csv_path, newline = "") as fh:
        csvreader = csv.reader(fh, delimiter = ",")
        next(csvreader, None)
    
        months = []
        for row in csvreader:
            #print(row[0].split('/')[0])
            months.append(row[0].split('/')[0])

        print(len(set(months)))
        print(


# In[81]:


# total amount of revenue gained over the entire period

def totalRevenue(csv_path):
    with open (csv_path, newline = "") as fh:
        csvreader = csv.reader(fh, delimiter = ",")
        next(csvreader, None)
    
        totRevenue = 0
        for row in csvreader:
            #print(int(row[1]))
            totRevenue += int(row[1])

        print(totRevenue)


# In[80]:


# the average change in revenue between months 
def avgChange(csvreader):
    with open (csv_path, newline = "") as fh:
        csvreader = csv.reader(fh, delimiter = ",")
        next(csvreader, None)
    
        # list that contains total revenue for each month
        monthRevenue = [0] * 12

        # compute revenue for each month
        for row in csvreader:
            month = int(row[0].split('/')[0]) - 1
            monthRevenue[month] += int(row[1])

        # compute average change in revenue between months
        totChange = 0
        for i in range(0, len(monthRevenue)-1):
            totChange += abs(monthRevenue[i] - monthRevenue[i+1])

        print(totChange/len(monthRevenue))
        


# In[79]:


# the maximum change in revenue (date and amount)
def maxChange(csvreader):
    with open (csv_path, newline = "") as fh:
        csvreader = csv.reader(fh, delimiter = ",")
        next(csvreader, None)
    
        # list that contains total revenue for each month
        monthRevenue = [0] * 12

        # compute revenue for each month
        for row in csvreader:
            month = int(row[0].split('/')[0]) - 1
            monthRevenue[month] += int(row[1])

        # compute average change in revenue between months
        maxChange = 0
        for i in range(0, len(monthRevenue)-1):
            change = abs(monthRevenue[i] - monthRevenue[i+1])

            if(change > maxChange):
                maxChange = change

        print(maxChange)


# In[78]:


#the minimum change in revenue (date and amount)
def minChange(csvreader):
    with open (csv_path, newline = "") as fh:
        csvreader = csv.reader(fh, delimiter = ",")
        next(csvreader, None)
    
        # list that contains total revenue for each month
        monthRevenue = [0] * 12

        # compute revenue for each month
        for row in csvreader:
            month = int(row[0].split('/')[0]) - 1
            monthRevenue[month] += int(row[1])

        # compute average change in revenue between months
        minChange = sys.maxsize
        for i in range(0, len(monthRevenue)-1):
            change = abs(monthRevenue[i] - monthRevenue[i+1])

            if(change < minChange):
                minChange = change

        print(minChange)

