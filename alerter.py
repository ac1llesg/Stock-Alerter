#!/usr/bin/env python
# coding: utf-8

# In[29]:


import bs4
import requests
from bs4 import BeautifulSoup as bs
from sys import stdout
from time import sleep
from playsound import playsound


# In[30]:


def parse(website):
    #Fetches price
    r = requests.get(str(website))
    soup = bs(r.text, "html.parser")
    price = soup.find("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find("span").text
    return price


# In[45]:



def alerter(website, alert_price):
    
    #initialize
    num = 1
    
    
    while True:
        
        #updates price
        price = float(parse(website))
        
        if price < float(alert_price):
            
            #alerts user if stock price is below your alert price
            stdout.write("\r Your stock fell below %s. It's now trading at %s."% (alert_price, price))
            playsound('alert.wav')
            stdout.flush()
            
        else:

            #Tells user that the code is running
            stdout.write("\rRunning..." + str(num))
            stdout.flush()

            num += 1


# In[46]:





# In[ ]:





# In[ ]:




