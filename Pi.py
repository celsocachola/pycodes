#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt


# In[2]:


N = 1000 # Total number of points
hit = 0 # counter
for i in range(N):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 < 1.0: 
        hit += 1
        plt.scatter(x, y)
pi_est_1 = 4 * hit / N
print("Pi:",pi_est_1)


# In[3]:


N = 10000 # Total number of points
hit = 0 # counter
for i in range(N):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 < 1.0: 
        hit += 1
pi_est_2 = 4 * hit / N
print("Pi:",pi_est_2)


# In[4]:


N = 100000 # Total number of points
hit = 0 # counter
for i in range(N):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 < 1.0: 
        hit += 1
pi_est_3 = 4 * hit / N
print("Pi:",pi_est_3)


# In[5]:


N = 1000000 # Total number of points
hit = 0 # counter
for i in range(N):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 < 1.0: 
        hit += 1
pi_est_4 = 4 * hit / N
print("Pi:",pi_est_4)


# In[6]:


N = 10
# Total number of points
hit = 0 # counter
for i in range(N):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 < 1.0: 
        hit += 1
pi_est_5 = 4 * hit / N
print("Pi:",pi_est_5)


# In[7]:


N = 100000000 # Total number of points
hit = 0 # counter
for i in range(N):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 < 1.0: 
        hit += 1
pi_est_6 = 4 * hit / N
print("Pi:",pi_est_6)


# In[8]:


N = 1000000000 # Total number of points
hit = 0 # counter
for i in range(N):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 < 1.0: 
        hit += 1
pi_est_7 = 4 * hit / N
print("Pi:",pi_est_7)


# In[9]:


plt.plot([pi_est_1,pi_est_2,pi_est_3,pi_est_4,pi_est_5,pi_est_6,pi_est_7])

