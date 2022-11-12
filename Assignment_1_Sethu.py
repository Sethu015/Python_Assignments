#!/usr/bin/env python
# coding: utf-8

# Declare a boolean value and store it in a variable.

# In[49]:


testValue = False
print(type(testValue).__name__)
print(id(testValue))


# Take one boolean value between 0 - 256.
# Assign it to two different variables.
# Check the id of both the variables.

# In[50]:


boolValue = bool(15)
firstVar = boolValue
secondVar = boolValue
print(id(firstVar))
print(id(secondVar))

#Python Caches the id for datatype boolean which have value and
#if same value is being used in another place the same id value will only be printed


# Arithmetic Operations on boolean data
# Take two different boolean values.
# Store them in two different variables.
# Do below operations on them:-
# Find sum of both values
# Find difference between them
# Find the product of both.
# Find value after dividing first value with second value
# Find the remainder after dividing first value with second value
# Find the quotient after dividing first value with second value
# Find the result of first value to the power of second value.

# In[52]:


firstValue = bool(0)
secondValue = bool(25)
print(firstValue + secondValue)
print(firstValue - secondValue)
print(firstValue * secondValue)
print(firstValue / secondValue)
print(firstValue % secondValue)
print(firstValue / secondValue)
print(pow(firstValue,secondValue))


# Comparison Operators on boolean values
# Take two different boolean values.
# Store them in two different variables.
# Do below operations on them:-
# Compare these two values with below operator:-
# Greater than, '>'
# less than, '<'
# Greater than or equal to, '>='
# Less than or equal to, '<='
# Observe their output(return type should be boolean)

# In[53]:


firstVar = True
secondVar = False
print(firstVar > secondVar)
print(firstVar < secondVar)
print(firstVar >= secondVar)
print(firstVar <= secondVar)


# Equality Operator
# Take two different boolean values.
# Store them in two different variables.
# Equate them using equality operators (==, !=)
# Observe the output(return type should be boolean)

# In[55]:


firstVal = False
secondVal = True
print(type(firstVal == secondVal).__name__)
print(type(firstVal != secondVal).__name__)


# In[57]:


firstValue = 25
secondValue = 20
thirdValue = 15
forthValue = 18
print(firstValue > secondValue and forthValue > thirdValue)
print(firstValue < secondValue and forthValue > thirdValue)
print(firstValue > secondValue and forthValue < thirdValue)
print(firstValue < secondValue and forthValue < thirdValue)
print(firstValue > secondValue or forthValue > thirdValue)
print(firstValue < secondValue or forthValue > thirdValue)
print(firstValue > secondValue or forthValue < thirdValue)
print(firstValue < secondValue or forthValue < thirdValue)
print(not firstValue > secondValue)
print(not firstValue < secondValue)


# In[ ]:




