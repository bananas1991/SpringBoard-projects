#!/usr/bin/env python
# coding: utf-8

# This exercise will require you to pull some data from the Qunadl API. Qaundl is currently the most widely used aggregator of financial market data.

# As a first step, you will need to register a free account on the http://www.quandl.com website.

# After you register, you will be provided with a unique API key, that you should store:

# In[1]:


# Store the API key as a string - according to PEP8, constants are always named in all upper case
API_KEY = ''


# Qaundl has a large number of data sources, but, unfortunately, most of them require a Premium subscription. Still, there are also a good number of free datasets.

# For this mini project, we will focus on equities data from the Frankfurt Stock Exhange (FSE), which is available for free. We'll try and analyze the stock prices of a company called Carl Zeiss Meditec, which manufactures tools for eye examinations, as well as medical lasers for laser eye surgery: https://www.zeiss.com/meditec/int/home.html. The company is listed under the stock ticker AFX_X.

# You can find the detailed Quandl API instructions here: https://docs.quandl.com/docs/time-series

# While there is a dedicated Python package for connecting to the Quandl API, we would prefer that you use the *requests* package, which can be easily downloaded using *pip* or *conda*. You can find the documentation for the package here: http://docs.python-requests.org/en/master/ 

# Finally, apart from the *requests* package, you are encouraged to not use any third party Python packages, such as *pandas*, and instead focus on what's available in the Python Standard Library (the *collections* module might come in handy: https://pymotw.com/3/collections/ ).
# Also, since you won't have access to DataFrames, you are encouraged to us Python's native data structures - preferably dictionaries, though some questions can also be answered using lists.
# You can read more on these data structures here: https://docs.python.org/3/tutorial/datastructures.html

# Keep in mind that the JSON responses you will be getting from the API map almost one-to-one to Python's dictionaries. Unfortunately, they can be very nested, so make sure you read up on indexing dictionaries in the documentation provided above.

# In[2]:


# First, import the relevant modules
import json
import requests


# In[3]:


# Now, call the Quandl API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned
sample_data = requests.get('https://www.quandl.com/api/v3/datasets/FSE/AFX_X/data.json?start_date=2015-12-12&end_date=2015-12-12'+API_KEY)


# In[4]:


# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure
sample_data.status_code


# In[5]:


type(sample_data)


# sample_data.shape()

# In[6]:


sample_data.json()


# In[ ]:





# These are your tasks for this mini project:
# 
# 1. Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
# 2. Convert the returned JSON object into a Python dictionary.
# 3. Calculate what the highest and lowest opening prices were for the stock in this period.
# 4. What was the largest change in any one day (based on High and Low price)?
# 5. What was the largest change between any two days (based on Closing Price)?
# 6. What was the average daily trading volume during this year?
# 7. (Optional) What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)

# In[9]:


#Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
data2017 = requests.get('https://www.quandl.com/api/v3/datasets/FSE/AFX_X/data.json?start_date=2017-01-01&end_date=2017-12-31'+API_KEY)


# In[10]:


#check the status
data2017.status_code


# In[11]:


#Convert the returned JSON object into a Python dictionary.
data_2017 = data2017.json()


# In[12]:


#check the type
type(data_2017)


# In[13]:


data_2017.keys()


# In[14]:


data_2017['dataset_data'].keys()


# In[15]:


data_2017['dataset_data']['column_names']


# In[23]:


# create empty lists for data we are going to use
open_2017 = []
high_2017 = []
low_2017 = []
close_2017 = []
traded_v_2017 = []
d_change_day = []
d_change_two_days = [0]


# In[25]:


# iterate through the data
for i in range(len(data_2017['dataset_data']['data'])):
    data_open = data_2017['dataset_data']['data'][i][1]
    data_close = data_2017['dataset_data']['data'][i][4]
    data_high = data_2017['dataset_data']['data'][i][2]
    data_low = data_2017['dataset_data']['data'][i][3]
    data_traded_v = data_2017['dataset_data']['data'][i][6]
    
    if isinstance (data_open, float):
        open_2017.append(data_open)
    if isinstance (data_high-data_low,float):
        d_change_day.append(data_high-data_low)
    if isinstance (data_close,float):
        close_2017.append(data_close)
    if isinstance (data_traded_v, float):
        traded_v_2017.append(data_traded_v)
    
    if i != 0 :
        d_change_two_days.append(close_2017[i]-close_2017[i-1])
        
    
    


# In[28]:


# Print the solutions
print('Highest opening price is:',max(open_2017))
print('Lowest opening price is:',min(open_2017))
print ('Largest change in any one day:', max(d_change_day))
print('Largest change in two consecutive days is:', max(d_change_two_days))


# In[32]:


#What was the average daily trading volume during this year
number_of_t = len(traded_v_2017)
total = sum(traded_v_2017)
avg = total / number_of_t
print ('Average daily trading volume during this year:', avg)


# In[33]:


# MEDIAN
d_trade_vol = sorted(traded_v_2017)
d_len = len(traded_v_2017)
if  d_len%2 == 0:
    med = traded_v_2017[int(d_len/2)]
else :
    med = (traded_v_2017[int(d_len/2)] + traded_v_2017[int(d_len/2 -1)]) * 0.5
    
print("The median trading volume is:", med)


# In[41]:


def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen-1) // 2
    
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index +1])/2.0


# In[35]:


traded_volume = traded_v_2017


# In[42]:


median(traded_volume)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




