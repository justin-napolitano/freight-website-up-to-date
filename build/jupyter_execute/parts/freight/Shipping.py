#!/usr/bin/env python
# coding: utf-8

# # US Shipping Routes and Ports Analysis
# 
# 
# This is a precursor project to one that will create a graph of rail, shipping, trucking, and air freight transport networks for analysis.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import plugins
import contextily as cx


# ## Data

# In[2]:


gisfilepath = "/Users/jnapolitano/Projects/freight.jnapolitano.io/source/data/shipping/Navigable_Waterway_Lines.geojson"

waterway_df = gpd.read_file(gisfilepath)

waterway_df.head()


# ### Checking Cooridindate System.  
# 
# The coordinate system must be in the epsg 3857 format to overlay.

# In[3]:


waterway_df.crs


# #### Converting to EPSG 3857 System

# In[4]:


df_wm = waterway_df.to_crs(epsg=3857)


# In[5]:


ax = df_wm.plot(figsize=(20, 20),column='RIVERNAME', alpha=0.5)
cx.add_basemap(ax, zoom=3)


# ### Impressions
# 
# The Gulf Waters are concentrated and dependent on non-US Ports.  For instance the Gulf-Carribean Access Point concentrates near the Yucatan penninsula.  There is also a major concentration near Cuba and the Dominican Republic. I would have considered Puerto Rico to be a more important shipping route.

# ## US Ports Data Set

# In[6]:


gisfilepath = "/Users/jnapolitano/Projects/freight.jnapolitano.io/source/data/shipping/Ports.geojson"

ports_df = gpd.read_file(gisfilepath)

ports_df


# In[7]:


ports_df.columns


# ### Impressions
# There are 24,1117 ports recorded in this dataset.  There are also 43 fields of data.  Columns of interests are Highway_No and Railway_No.  I would like to investigate this further.

# #### Converting to EPSG 3857 System

# In[8]:


ports_df_wm = ports_df.to_crs(epsg=3857)
ports_df_wm.COMMODITIE.unique()


# In[9]:


ax = ports_df_wm.plot(figsize=(20, 20), alpha=1, column='COMMODITIE')
cx.add_basemap(ax, zoom=4)


# ```{eval-rst}
# 
# .. index::
#    single: US Ports Map Interactive
# 
# ```
# ### US Ports Map

# In[10]:


#ports_df_wm.explore()

ports_map = ports_df_wm.explore(column="COMMODITIE", # make choropleth based on "COMMODITIE" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"),
     marker_kwds= dict(radius=3),
     tooltip='COMMODITIE',
     legend = False # use black outline)
     #scheme = 'EqualInterval',
     #k = 4

)
ports_map


# ### Results
# 
# It is interesting to see all of the ports in the United States, but I notice that the majority are small ports registered by organizations to move goods to market.  For the purpose of this analysis there is too much noise to yield information.

# ## Major US Ports Data Set

# In[11]:


gisfilepath = "/Users/jnapolitano/Projects/freight.jnapolitano.io/source/data/shipping/Major_Ports.geojson"

major_ports_df = gpd.read_file(gisfilepath)

major_ports_df


# In[12]:


major_ports_df.columns


# ### Impressions
# 
# This data is far more managable.  It also contains data relating to freight volumes.

# In[13]:


major_ports_df_wm = major_ports_df.to_crs(epsg=3857)


# ```{eval-rst}
# 
# .. index::
#    single: Major US Ports Map Interactive
# ```
# 
# ### Major Us Ports Map

# In[14]:


major_ports_map = major_ports_df.explore(column="GRAND_TOTA", # make choropleth based on "COMMODITIE" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=3),
     tooltip=['PORT_NAME','FOREIGN_TO', 'DOMESTIC','GRAND_TOTA'],
     legend = True, # use black outline)
     scheme = 'EqualInterval',
     #k = 4

)
major_ports_map


# ## Petrolium Ports Data

# In[15]:


gisfilepath = "/Users/jnapolitano/Projects/freight.jnapolitano.io/source/data/Petroleum_Ports.geojson"

petrolium_ports_df = gpd.read_file(gisfilepath)

petrolium_ports_df


# In[16]:


petrolium_ports_df.columns


# In[17]:


petrolium_ports_wm = petrolium_ports_df.to_crs(epsg=3857)


# ```{eval-rst}
# 
# .. index::
#    single: Petrolium Ports Map Interactive
# ```
# 
# ### Petrolium Ports by KTONS Gas Map

# In[18]:


#### Removing KTONS_GAS == 0 From Data Frame

gas_ports_df=petrolium_ports_df.loc[petrolium_ports_df['KTONS_GAS'] > 0]
gas_ports_df


# In[19]:


gas_ports_map = gas_ports_df.explore(column="KTONS_GAS", # make choropleth based on "COMMODITIE" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     tooltip=['NAME','KTONS_GAS', 'OPERATOR','WEBSITE'],
     legend = True, # use black outline)
     scheme = 'NaturalBreaks',
     k = 6

)
gas_ports_map


# ### Gas Ports Heat Map

# In[20]:


gas_heat_data = [[point.xy[1][0], point.xy[0][0]] for point in gas_ports_df.geometry ]
#

gas_density_map = folium.Map(location = [30, -90], tiles='Cartodb dark_matter', zoom_start = 4, blur= 1)

gas_heat_layer = plugins.HeatMap(data = gas_heat_data, show=True)
gas_heat_layer.add_to(gas_density_map)

gas_density_map

