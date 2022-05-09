#!/usr/bin/env python
# coding: utf-8

# # US Logistics Network Analysis

# In[1]:



import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import contextily as cx
import rtree
from zlib import crc32
import hashlib
from shapely.geometry import Point, LineString, Polygon


# ## Rail Facilities by Nearest Ports

# ### Intermodal Rail Data

# In[2]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/intermodal/Intermodal_Freight_Facilities_RailTOFCCOFC.geojson"

rail_to_all_df = gpd.read_file(gisfilepath)

rail_to_all_df = rail_to_all_df.to_crs(epsg=3857)

rail_to_all_df


# ### Major Ports Data

# In[3]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/shipping/Major_Ports.geojson"
major_ports_df = gpd.read_file(gisfilepath)
major_ports_df = major_ports_df.to_crs(epsg=3857)

major_ports_df


# #### Hashing Ports to Unique IDS

# In[4]:


def bytes_to_float(b):
    return float(crc32(b) & 0xffffffff) / 2**32

def str_to_float(s, encoding="utf-8"):
    return bytes_to_float(s.encode(encoding))


# In[5]:


major_ports_df['hash'] = major_ports_df['PORT_NAME']
major_ports_df['hash'] = major_ports_df['hash'].map(lambda x: str_to_float(x))
#major_transit_nodes.hash.apply(lambda x: str_to_float(x))
major_ports_df['port_geo']=major_ports_df['geometry']
major_ports_df


# #### Creating Ports Map
# 

# In[6]:


major_ports_map =major_ports_df.explore(
    column="hash", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap='Reds', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     tooltip=['PORT_NAME','GRAND_TOTA'],
     legend =False, # use black outline)
     categorical=True,
    )


major_ports_map


# ### Intermodal Rail Stations Joined by Nearest Major Port

# In[7]:


major_transit_nodes = rail_to_all_df.sjoin_nearest(major_ports_df)
major_transit_nodes.drop(columns=['OBJECTID_right', 'index_right','OBJECTID_1','OBJECTID_left','PORT_left'], inplace=True)
print(major_transit_nodes.columns)
major_transit_nodes


# ```{eval-rst}
# 
# .. index::
#    single: Rail Facilities by Port Interactive Map
# 
# ```

# ### Rail Facilities by Port Interactive Map
# 

# In[8]:


major_rail_facilities_map =major_transit_nodes.explore(
    column="hash", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap='Reds', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     tooltip=['PORT_NAME','GRAND_TOTA'],
     legend =False, # use black outline)
     categorical=True,
     legend_kwds={'label': "Population by Country",
                        'orientation': "horizontal"}
    )


major_rail_facilities_map


# ## Air Freight to Truck Facilites by Major Port

# In[9]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/intermodal/Intermodal_Freight_Facilities_Air-to-Truck.geojson"
air_freight_to_truck_df = gpd.read_file(gisfilepath)
air_freight_to_truck_df = air_freight_to_truck_df.to_crs(epsg=3857)

air_freight_to_truck_df


# ### Air Freight Hubs joined by Major Ports

# In[10]:


major_air_freight = air_freight_to_truck_df.sjoin_nearest(major_ports_df)

major_air_freight.drop(columns=['OBJECTID_right', 'index_right','OBJECTID_1','OBJECTID_left'], inplace=True)
print(major_air_freight.columns)

major_air_freight


# ```{eval-rst}
# 
# .. index::
#    single: Air Fright Hubs by Nearest Ports Interactive Map
# 
# ```

# ### Air Freight Hubs by Nearest Major Port Port Map

# In[11]:


major_air_freight.explore(
    column="hash", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap='Reds', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     tooltip=['PORT_NAME','FACILITY_C','LOCID'],
     legend =False, # use black outline)
     categorical=True)


# ## Shipping Networks

# ### Shipping Data

# In[12]:


gisfilepath = "//Users/jnapolitano/Projects/rail-mapping/shipping/Navigable_Waterway_Lines.geojson"
shipping_network = gpd.read_file(gisfilepath)
shipping_network = shipping_network.to_crs(epsg=3857)

shipping_network


# ### Shipping Networks by Major Ports

# In[13]:


port_shipping = shipping_network.sjoin_nearest(major_ports_df)
port_shipping.drop(columns = ['OBJECTID_left','DIR', 'ANODE', 'BNODE', 'ID_left', 'AMILE', 'BMILE', 'LENGTH1', 'LENGTH_SRC', 'SHAPE_SRC', 'GEO_CLASS', 'FUNC_CLASS','OBJECTID_1','CHART_ID', 'index_right', 'NUM_PAIRS', 'CHART_ID', 'DATE_MOD', 'WHO_MOD', 'OBJECTID_right','ID_right'],inplace=True)
print(port_shipping.columns)
port_shipping


# ```{eval-rst}
# 
# .. index::
#    single: Shipping Routes by Major Port Interactive Map
# 
# ```

# ### Shipping Routes by Major Port Interactive Map

# In[14]:


port_shipping.explore(
    column="hash", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap='Reds', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     tooltip=['PORT_NAME','RIVERNAME'],
     legend =False, # use black outline)
     categorical=True)


# ## Coastal Pipeline Networks

# ### Pipeline Data

# In[15]:


gisfilepath = "/Users/jnapolitano/Projects/data/energy/Pipelines.gdb"
terminal_network = gpd.read_file(gisfilepath)
terminal_network = terminal_network.to_crs(epsg=3857)

terminal_network.columns


# ```{eval-rst}
# 
# .. index::
#    single: Coastal Pipeline Interactive Map
# 
# ```

# ### Coastal Piplines Major Port Interactive Map

# In[16]:


terminal_network.explore(
    column="PROD_CODE", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap='Blues', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     tooltip=['SDE_COMPAN','Prod_Descpt'],
     legend =True, # use black outline)
     categorical=True)


# In[ ]:




