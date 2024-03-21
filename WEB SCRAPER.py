#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


# In[13]:


headers ="""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"""


# In[59]:


mobile_name=[]


# In[60]:


pages = np.arange(1,4060,24)


# In[61]:


for page in pages:
    page = requests.get("https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=8486e085-7f64-4f1f-ae25-bfa26699fdc4&p%5B%5D=facets.type%255B%255D%3DSmartphones&p%5B%5D=facets.brand%255B%255D%3DApple&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DIQOO&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DMi")
    soup = BeautifulSoup(page.text , 'html.parser')
    mobile_data = soup.findAll('div' , attrs = {'class' : '_4rR01T'})
    
    for store in mobile_data:
        name = store.text
        mobile_name.append(name)


# In[62]:


print(len(mobile_name))


# In[63]:


mobile = pd.DataFrame({"Mobile Name" : mobile_name})


# In[64]:


mobile


# In[65]:


mobile.to_csv("ad.csv")


# In[ ]:




