#!/usr/bin/env python
# coding: utf-8

# In[9]:


import webbrowser as wb
import pyautogui as pg
import time
site="https://web.whatsapp.com/"
wb.open(site,new=2)
time.sleep(10)
pg.typewrite("0009")
pg.press("enter")
time.sleep(10)
for i in range (10):
    pg.typewrite("Hi I am Bot")
    pg.press("enter")


# In[ ]:




