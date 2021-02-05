#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[2]:


from arcgis import *
gis = GIS("home")


# #### Now you are ready to start!

# In[24]:


# Item Added From Toolbar
# Title: Byways_Lab0 | Type: Feature Service | Owner: and04671_UMN

from arcgis import features
base_map = gis.map('Minnesota')
Raw_Byway = gis.content.search ('Byways')[2]


# In[28]:


out = features.use_proximity.create_buffers(input_layer = Raw_Byway,
                                           distances = [4],
                                           field = None,
                                           units = 'Miles',
                                           output_name = 'Buffer_Byway')


# In[29]:


out

