#!/usr/bin/env python
# coding: utf-8

# In[31]:


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import xarray as xr
import numpy as np


# In[58]:


app = Dash(__name__)
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
DS = xr.open_dataset("data/ape_5000_55_0S_atm_2d_ml.ym.zm.nc",decode_times=False)
data_sit=DS.sit.squeeze()
data_hs=DS.hs_icecl.squeeze() + data_sit


# In[59]:


sit = data_sit.values.flatten()
hs = data_hs.values.flatten()
print(len(sit))
time=np.repeat(np.arange(0,len(data_sit.time),1),len(data_sit.lat))
print(len(time))
lat=np.tile(data_sit.lat.values,len(data_sit.time))
print(len(lat))


# In[70]:


varlist=["sit","hs"]
nvar=len(varlist)
time_multivar=np.tile(time,nvar)
lat_multivar=np.tile(lat,nvar)
var=np.repeat(varlist,len(time))
thickness = np.append(sit,hs)
print(len(time_multivar))
print(len(thickness))
print(len(lat_multivar))
print(len(var))


# In[63]:


np.tile([0,1,2],3)


# In[72]:


#df = pd.DataFrame({
#    "sit": sit,
#    "hs": hs,
#    "time": time,
#    "lat": lat
#})

df = pd.DataFrame({
    "thickness": thickness,
    "time": time_multivar,
    "lat": lat_multivar,
    "var": var
})


# In[75]:


#fig = px.line(df, x="lat", y="sit", title='Sea-ice thickness', animation_frame="time", range_y=(0,80))
fig = px.bar(df, x='lat', y="thickness", color='var', hover_data=['var'], range_y=(0,100), title='Snowball test', animation_frame="time", color=("blue", "green"))


# In[74]:


app = Dash(__name__)
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




