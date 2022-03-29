#!/usr/bin/env python
# coding: utf-8

# In[5]:


#python program to reverse a string
rev_string=' '
def rev(i,string):
    global rev_string
    rev_string=i+rev_string
    return rev_string
string="1234abcd"
for i in string:
    reverse=rev(i,string)
print(reverse)
    


# In[ ]:





# In[ ]:




