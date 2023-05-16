#!/usr/bin/env python
# coding: utf-8

# Q1. What is the difference between __getattr__ and __getattribute__?
# 

# The main difference between __getattr__ and __getattribute__ is that if the attribute was not found by the usual way then __getattr__ is used.
# 
# Whereas the __getattribute__ is used before looking at the actual attributes on the object. You will have to use it more consciously otherwise very easily you can end up in infinite recursions.

# Q2. What is the difference between properties and descriptors?
# 

# Descriptors are a low-level mechanism that lets you hook into an object's attributes being accessed. 
# 
# Properties are a high-level application of this; that is, properties are implemented using descriptors.

# Q3. What are the key differences in functionality between __getattr__ and __getattribute__, as well as properties and descriptors?
# 

# The main difference between __getattr__ and __getattribute__ is that __getattr__ is only called when the attribute cannot be found through normal attribute lookup, while __getattribute__ is always called first for every attribute access.
# 
#  properties are a high-level way to customize attribute access using methods,
#  
#  while descriptors are lower-level objects that allow fine-grained control over attribute access by implementing the descriptor protocol with __get__, __set__, and __delete__ methods.

# In[ ]:




