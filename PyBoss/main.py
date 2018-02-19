
# coding: utf-8

# In[33]:


# https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[36]:


def parseCSV(file_name, delimeter=","):
    """
    reads a csv and yields a list for each line
    """
    with open(file_name, "r") as fh:
        header = fh.readline().strip().split(delimeter)
        lol = []
        for line in fh:
            lol.append(line.strip().split(delimeter))
        return header, lol
        


# In[49]:


def writeCSV(file_name, write_list, delimeter=","):
    """
    writes to a csv file from a list of lists (row)
    """
    with open(file_name, "w") as fh:
        for row in write_list:
            fh.write(delimeter.join(row)+'\n')  # join output lists as str sep by ','


# In[50]:


def main():
    filename_in = 'employee_data1.csv'  # specified from user
    fn = filename_in.split('.')
    filename_out = fn[0] + '_modified.' + fn[1]
    parse = parseCSV(filename_in)
    lol = [parse[0]]
    for row in parse[1]:
        emp_id = row[0]
        names = row[1].split(' ')
        first, last = names[0], names[1]
        dob = row[2].split('-')
        dob_str = '/'.join([dob[1], dob[2], dob[0]])  # join is opposite of split
        ssn = '***-**-' + row[3][-4:]
        state = us_state_abbrev[row[4]]
        lol.append([emp_id, first, last, dob_str, ssn, state])
    writeCSV(filename_out, lol)
    


# In[51]:


main()

