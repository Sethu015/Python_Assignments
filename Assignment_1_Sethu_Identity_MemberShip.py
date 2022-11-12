#!/usr/bin/env python
# coding: utf-8

# What is the output of expression inside the print statement. Cross
# check before running the program.
# a = True
# b = True
# print (a is b) #True or False? #
# print (a is not b) #True or False?
# a = False
# b = False
# print (a is b) #True or False?
# print (a is not b) #True or False?

# In[4]:


a = True
b = True
print(a is b) #It will return True
print(a is not b) # It will return False


# Membership operation
# in, not in are two membership operators and it returns boolean value
# print ( True in [ 10 , 10.20 , 10 + 20j , 'Python' , True ])
# print ( False in ( 10 , 10.20 , 10 + 20j , 'Python' , False ))
# print ( True in { 1 , 2 , 3 , True })
# print ( True in { True : 100 , False : 200 , True : 300 })
# print ( False in { True : 100 , False : 200 , True : 300 })

# In[12]:


print ( True in [ 10 , 10.20 , 10 + 20j , 'Python' , True ]) #It Returns True
print ( False in ( 10 , 10.20 , 10 + 20j , 'Python' , False )) #It Returns True
print ( True in { 1 , 2 , 3 , True }) #It Returns True
print ( True in { True : 100 , False : 200 , True : 300 }) #It Returns True even if key matches
print ( False in { True : 100 , False : 200 , True : 300 }) #It Returns True even if key matches


# In[ ]:




