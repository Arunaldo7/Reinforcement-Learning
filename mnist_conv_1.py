#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd;
import numpy as np;

import matplotlib.pyplot as plt;


# In[2]:


from tensorflow.keras.datasets import mnist;


# In[3]:


(X_train, y_train), (X_test, y_test) = mnist.load_data();


# In[4]:


X_train.shape


# In[5]:


sample_image = X_train[0]


# In[6]:


plt.imshow(sample_image);


# In[7]:


from tensorflow.keras.utils import to_categorical;


# In[8]:


y_example = to_categorical(y_train);


# In[9]:


y_example[0]


# In[10]:


y_train


# In[11]:


from tensorflow.keras.models import Sequential;
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPool2D;


# In[12]:


X_train = X_train / 255;
X_test = X_test / 255;

y_cat_train = to_categorical(y_train, 10);
y_cat_test = to_categorical(y_test,10)


# In[13]:


X_train.shape


# In[14]:


X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1);
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1);


# In[15]:


X_train.shape


# In[16]:


model = Sequential();

model.add(Conv2D(filters = 2, kernel_size = (4,4), input_shape = (28,28,1), activation = "relu"));
model.add(MaxPool2D(pool_size = (2,2)));

model.add(Flatten());

model.add(Dense(128, activation = "relu"));

model.add(Dense(10, activation = "softmax"));

model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"]);


# In[17]:


from tensorflow.keras.callbacks import EarlyStopping;


# In[18]:


early_stop = EarlyStopping(monitor = "loss", patience = 1);


# In[ ]:
print("fitting model")

model.fit(X_train, y_cat_train, epochs = 10, callbacks = [early_stop],
         verbose = 1)


# In[ ]:




