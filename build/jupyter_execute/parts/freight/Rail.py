#!/usr/bin/env python
# coding: utf-8

# # Rail Analysis
# 
# Mapping Rail Lines and Rail Nodes in the United States.  
# 
# This is a precursor project to one that will create a graph of rail, shipping, trucking, and air freight transport networks for analysis. 
# 
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import contextily as cx
from mpl_toolkits.axes_grid1 import make_axes_locatable


# The error above is unimportant for my use case.  It is an unfortunate reality of Python Programming that package updates can break compatability layers.

# ## Rail Line Dataset Analysis
# 
# 

# ### Loading the Rail Line Data
# 

# In[2]:


shapefilepath = "/Users/jnapolitano/Projects/freight.jnapolitano.io/source/data/North_American_Rail_Lines/North_American_Rail_Lines.shp"

line_df = gpd.read_file(shapefilepath)



line_df.head()


# ### Checking Cooridindate System.  
# 
# The coordinate system must be in the epsg 3857 format to overlay.

# In[3]:


line_df.crs


# ### Converting to EPSG 3857 System 
# 
# 

# In[4]:


line_wm = line_df.to_crs(epsg=3857)


# ```{eval-rst}
# 
# .. index::
#    single: Rail Lines North America Map
# 
# ```

# ## Rail Lines in US, Canada, Mexico Map by Rail Owner

# In[5]:



us_map = line_wm.plot(column='RROWNER1',figsize=(15,15))
cx.add_basemap(us_map, zoom=6)


# ### Data Fields

# In[6]:


line_wm.columns


# ## Texas Rail Lines Data
# 
# Texas is an important freight destination.  The state possess many natural important ports and freight stations.  
# 
# 
# 

# ### Filtering the data set for Texas state Lines.
# 
# FIPS codes can be found at https://www.nrcs.usda.gov/wps/portal/nrcs/detail/?cid=nrcs143_013696
# 
# Texas is recognized as code 48.  

# In[7]:



#Getting Unique values to identify 48 is in the set 
print(line_wm['STFIPS'].unique())
#48 is a strin in the dataset do not compare it to an integer!!
texas_lines_df = line_wm.loc[line_wm['STFIPS'] == '48']
#print(texas_lines_df)
#print(texas_lines_df)


# ```{eval-rst}
# 
# .. index::
#    single: Texas Rail Map Non-Interactive 
# 
# ```

# ### Texas Non-Interactive Map

# In[8]:


ax = texas_lines_df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k', markersize = .5)
cx.add_basemap(ax, zoom=6)


# ```{eval-rst}
# 
# .. index::
#    single: Texas Rail Map Interactive
# 
# ```

# ### Texas Rail Map Interactive Map.

# In[9]:


#texas_lines_df.explore()

texas_map = texas_lines_df.explore(column="RROWNER1", # make choropleth based on "BoroName" column
     popup=True, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),# use black outline)
     #scheme = 'EqualInterval',
     #k = 4

)
texas_map


# 
