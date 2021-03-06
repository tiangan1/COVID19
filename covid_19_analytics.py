# -*- coding: utf-8 -*-
"""Covid-19_analytics

Automatically generated by Colaboratory.


"""

import plotly.graph_objects as go
import pandas as pd

Ab = pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/Covid_19/Abbreviation.csv')

Ab = Ab.dropna()

Ab.shape

df_covid_us_sum = NewData.groupby(['State'])['Confirmed'].agg('sum').reset_index()
df_covid_us_sum_merge = NewData.merge(df_us_states, left_on='Province_State', right_on='State')
df_covid_us_sum = df_covid_us_sum_merge[['State','Abbreviation','Confirmed']]
df_covid_us_sum.sort_values('Confirmed',ascending=False).head(10)

#testing_data = pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/Covid-2019_analystics/testing.csv', header=1)
#testing_data = testing_data.iloc[9:-1,:]

#import datetime

#testing_data.specimen_date = pd.date_range('2020-03-01', periods=30, freq='D')
#testing_data.reset_index(drop=True, inplace=True)

#testing_data['confirm_rate'] = testing_data['Number_confirmed'] / testing_data['Number_tested']
#testing_data

from google.colab import files
NewData.to_csv('Covid_19.csv') 
files.download('Covid_19.csv')

"""# Covid-19 Mapping"""

from google.colab import drive
drive.mount('/content/gdrive')

import pandas as pd
import numpy as np

data = pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/Covid-19/US_covid19.csv')

data = data.drop('Unnamed: 0', axis =1)
data.head()

data.describe()

import plotly.express as px

mapbox_access_token = 'pk.eyJ1IjoiZmlzaGVlcCIsImEiOiJjazgwcXd5amIwMnRtM2ZwNDR5OHRjb2Q1In0.wUN67xk4G_3OYy9-tqoqgA'
px.set_mapbox_access_token(mapbox_access_token)
fig = px.scatter_mapbox(data, lat="Lat", lon="Long_", size="Confirmed",
                        size_max=100, zoom=4, 
                        hover_data=['Combined_Key', 'Deaths', 'Population'], 
                        width=1800, height=1000)

fig.show()

import plotly
plotly.__version__

import chart_studio.plotly as py
import chart_studio.tools as tls

usrname = 'ryanzy'
key = 'Mh539mReURbPeNqyub42'

tls.set_credentials_file(username=usrname, api_key=key)

py.plot(fig, filename='fig1', auto_open=False)

pip install geopandas==0.3.0

pip install pyshp==1.2.10

pip install shapely==1.6.3

pip install plotly-geo

import colorlover as cl
from IPython.display import HTML
HTML(cl.to_html( cl.flipper()['seq']['3'] ))

colors = cl.scales['9']['seq']['PuRd']
print('Color we chose in this notebook:\n')
HTML(cl.to_html(colors))

import plotly.figure_factory as ff

import numpy as np
import pandas as pd

endpts = [100, 2000, 4000, 8000, 16000, 20000, 30000]
fips = data['FIPS'].tolist()
values = data['Confirmed'].tolist()


fig = ff.create_choropleth(
    fips=fips, values=values, scope=['usa'],
    binning_endpoints=endpts, colorscale=colors[1:],
    show_state_data=False,
    show_hover=True,
    asp = 2.9,
    title_text = 'USA Covid-19',
    legend_title = '# Confirmed'
)
fig.layout.template = None
fig.show()

data['county'] = np.NAN
for i in range(len(data)):
    data['county'][i] = data.Combined_Key.str.split(',')[i][0]

data.set_index('county', inplace=True)

data2 = data.loc[:, ['Confirmed', 'Deaths', 'Population']]

data2.isna().any()

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
norm_data = scaler.fit_transform(data2)

from sklearn.decomposition import PCA
from sklearn.manifold import LocallyLinearEmbedding as LLE
from sklearn.manifold import TSNE
import umap

pca_data = PCA().fit_transform(norm_data)

# LLE
lle = LLE(n_neighbors=200, n_components=2)
lle_data = lle.fit_transform(norm_data)

# t-SNE
tsne = TSNE(n_components=2, perplexity=10)
tsne_data = tsne.fit_transform(norm_data)

# UMAP
umap_ = umap.UMAP(n_neighbors=20, metric='manhattan',
                init='random', min_dist=0.06, spread=3.0)
umap_data = umap_.fit_transform(norm_data)

from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2, 
                    subplot_titles=("PCA", "LLE", "T-SNE", "UMAP"))

# plot PCA
fig.add_trace(go.Scatter(
    x=pca_data[:, 0],
    y=pca_data[:, 1],
    mode="markers+text",
    marker_color='red',
    marker_symbol='circle',
    text=list(data.index),
    textposition="top center",
    textfont=dict(color="red")
),row=1, col=1)

# Plot LLE
fig.add_trace(go.Scatter(
    x=lle_data[:, 0],
    y=lle_data[:, 1],
    mode="markers+text",
    marker_color='red',
    marker_symbol='circle',
    text=list(data.index),
    textposition="top center",
    textfont=dict(color="red")
),row=1, col=2)

# Plot T-SNE
fig.add_trace(go.Scatter(
    x=tsne_data[:, 0],
    y=tsne_data[:, 1],
    mode="markers+text",
    marker_color='red',
    marker_symbol='circle',
    text=list(data.index),
    textposition="top center",
    textfont=dict(color="red")
),row=2, col=1)

#Plot UMAP
fig.add_trace(go.Scatter(
    x=umap_data[:, 0],
    y=umap_data[:, 1],
    mode="markers+text",
    marker_color='red',
    marker_symbol='circle',
    text=list(data.index),
    textposition="top center",
    textfont=dict(color="red")
),row=2, col=2)

# Update xaxis properties
fig.update_xaxes(title_text="$PC_{1}$", row=1, col=1)
fig.update_xaxes(title_text="$LLE_{1}$", row=1, col=2)
fig.update_xaxes(title_text="$T-SNE_{1}$", row=2, col=1)
fig.update_xaxes(title_text="$UMAP_{1}$", row=2, col=2)

# Update yaxis properties
fig.update_yaxes(title_text="$PC_{2}$", row=1, col=1)
fig.update_yaxes(title_text="$LLE_{2}$", row=1, col=2)
fig.update_yaxes(title_text="$T-SNE_{2}$", row=2, col=1)
fig.update_yaxes(title_text="$UMAP_{2}$", row=2, col=2)

# Edit layout
fig.update_layout(
    height=2200,
    width=2000,
)

fig.show()

"""# Mapping"""

import pandas as pd

confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
death = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')
death

confirmed['county'] = confirmed.Combined_Key.map(lambda x : x.split(',')[0])
death['county'] = death.Combined_Key.map(lambda x : x.split(',')[0])

confirmed = confirmed.iloc[:, 8:]
death = death.iloc[:, 8:]
confirmed.insert(0, 'County', confirmed.county)
death.insert(0, 'County', death.county)
confirmed.drop(columns=['Combined_Key', 'county'], inplace=True)
death.drop(columns=['Combined_Key', 'county'], inplace=True)

confirmed.drop(confirmed.iloc[:, 3:42], inplace=True, axis=1)
death.drop(death.iloc[:, 3:42], inplace=True, axis=1)

confirmed = confirmed.melt(confirmed.columns[0:3])
confirmed

death = death.melt(death.columns[0:4])

death

confirmed.columns = ['County', 'Lat', 'Long_', 'Date', 'Confirmed']
death.columns = ['County', 'Lat', 'Long_', 'Population', 'Date', 'Death']

confirmed

data = pd.merge(confirmed, death, on=['County', 'Lat', 'Long_', 'Date'])
data



data.Date = pd.to_datetime(data.Date, format='%m/%d/%y')

data.to_excel('Covid-19_data.xlsx')

data1 = data.iloc[:5000, :]

from google.colab import files

data1.to_csv('Covid-19_map_data.csv')

files.download("Covid-19_map_data.csv")

data.Date.drop_duplicates()



import plotly.express as px

mapbox_access_token = 'pk.eyJ1IjoiZmlzaGVlcCIsImEiOiJjazgwcXd5amIwMnRtM2ZwNDR5OHRjb2Q1In0.wUN67xk4G_3OYy9-tqoqgA'
px.set_mapbox_access_token(mapbox_access_token)
fig_map = px.scatter_mapbox(data, lat="Lat", lon="Long_",size="Confirmed",
                            color='Confirmed',
                        size_max=100, zoom=4, center=dict(lat=37.09024, 
                                                          lon=-95.712891), 
                        animation_frame='Date',
                        hover_data=['County', 'Confirmed', 'Death'])

fig_map.update_layout(width=1800,height=1000)
fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


#update frame speed
frame_speed = 60 * 1000 / len(data.Date.drop_duplicates())
fig_map.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = frame_speed

#update different layouts
fig_map.layout.sliders[0].currentvalue.font.color="indianred"
fig_map.layout.sliders[0].currentvalue.font.size=30

fig_map.show()

"""# States data"""

pip install BeautifulSoup4

pip install selenium

!apt-get update

from bs4 import BeautifulSoup
from selenium import webdriver

!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=chrome_options)

url ='https://www.cdc.gov/covid-data-tracker/index.html'

driver.get(url)
         
res = driver.page_source

response = BeautifulSoup(res, 'html.parser')

datas = response.find('table', class_='wtable')

datas

rows=[]
columns_name=['Jurisdiction','Total Cases','Deaths']

for data in datas:
  data= datas.find_all('td')
  if len(data)==0:
    continue
  for i in range(0,int(len(data)/3),3):
    Jurisdiction=data[i].getText()
    Total_Cases=data[i+1].getText()
    Deaths=data[i+2].getText()
    rows.append([Jurisdiction,Total_Cases,Deaths])

import pandas as pd
df=pd.DataFrame(rows,columns=columns_name)
df

from google.colab import drive
drive.mount('/content/gdrive')

df.to_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/UnitedStates_COVID-19_CasesReported.csv')

"""# Long Island"""

pip install BeautifulSoup4

pip install selenium

!apt-get update

from bs4 import BeautifulSoup
from selenium import webdriver

!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=chrome_options)

url ='https://nassau-county.maps.arcgis.com/apps/opsdashboard/index.html#/3545ec3d3a3e4ac1babe7d4714fedb56'

driver.get(url)
         
res = driver.page_source

response = BeautifulSoup(res, 'html.parser')

datas = response.find('div', class_='widget-body flex-fluid full-width flex-vertical overflow-y-auto overflow-x-hidden')

datas

rows=[]
columns_name=['Community','Total Cases']

for data in datas:
  data= datas.find_all('p')
  if len(data)==0:
    continue
for i in range(0,int(len(data)),2):
  Community=data[i].getText()
  Total_Cases=data[i+1].getText()
  rows.append([Community,Total_Cases])

import pandas as pd
df=pd.DataFrame(rows,columns=columns_name)
df

from google.colab import drive
drive.mount('/content/gdrive')

df.to_csv('/content/gdrive/My Drive/Colab Notebooks/Covid-19/Nassaucounty_COVID-19_CasesReported_7-15_5pm.csv')

url ='https://gis.suffolkcountyny.gov/portal/apps/opsdashboard/index.html#/f39eb4a7be7b4fbb9ee6d99d1b6e0b89'

driver.get(url)
         
res = driver.page_source

response = BeautifulSoup(res, 'html.parser')

datas = response.find('div', class_='widget flex-vertical full-height list-widget ember-view',id='ember41')

datas

rows=[]

for data in datas:
  data= datas.find_all('p')
  if len(data)==0:
    continue
for i in range(0,int(len(data))):
  data1=data[i].getText()
  rows.append(data1)

rows=rows[1:]

rows

import pandas as pd
df1=pd.DataFrame(rows)
df1

df2=df1[0].str.split('(',expand=True)

df3=df2[1].str.split(')',expand=True)

df4=df2[0].str.split(' ',expand=True,n=1)

df4[2]=df3[0]

df4.rename(columns={0:'Total Cases', 1:'Community',2:'Case/1k'})

df4.to_csv('/content/gdrive/My Drive/Colab Notebooks/Covid-19/Suffolkcounty_COVID-19_CasesReported_5-24_1pm.csv')

import pandas as pd
import csv

confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
death = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')
confirmed

confirmed['county'] = confirmed.Combined_Key.map(lambda x : x.split(',')[0])
death['county'] = death.Combined_Key.map(lambda x : x.split(',')[0])

confirmed

C_confirmed = confirmed[confirmed['county']=='Nassau']
C_confirmed=C_confirmed.append(confirmed[confirmed['county']=='Suffolk'])
LI_confirmed=C_confirmed[confirmed['Province_State']=='New York'].reset_index(drop=True)
LI_confirmed=pd.DataFrame.transpose(LI_confirmed)
LI_confirmed=LI_confirmed.rename(columns={ 0 :'Nassau', 1 :'Suffolk'})
LI_confirmed=LI_confirmed.iloc[8:]
LI_confirmed=LI_confirmed.drop(index='county')

LI_confirmed

LI_confirmed.to_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/LI_COVID-19_CasesReported.csv')

from google.colab import drive
drive.mount('/content/drive')

import plotly.graph_objects as go

import pandas as pd

# Load dataset
df = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/LI_COVID-19_CasesReported.csv')
df = df.iloc[3:]
df = df.rename(columns={'Unnamed: 0':'Date'})

# Initialize figure
fig = go.Figure()

# Add Traces

fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=list(df.Nassau),
               name="Nassau",
               line=dict(color="#33CFA5")))

fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=list(df.Suffolk),
               name="Suffolk",
               line=dict(color="#F06A6A")))

# Add Annotations and Buttons
fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Long Island",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "long Island"}]),
                dict(label="Nassau",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "Nassau"}]),
                dict(label="Suffolk",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title": "Suffolk"}])]))])

# Set title
fig.update_layout(title_text="Long island(7/14/20)")

fig.show()

"""# Long Island Mapping"""

import plotly
plotly.__version__

pip install plotly-geo

import colorlover as cl
from IPython.display import HTML
HTML(cl.to_html( cl.flipper()['seq']['3'] ))
colors = cl.scales['9']['seq']['PuRd']
print('Color we chose in this notebook:\n')
HTML(cl.to_html(colors))

pip install geopandas==0.3.0

pip install pyshp==1.2.10

pip install shapely==1.6.3

import numpy as np
import pandas as pd

data = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/Nassaucounty_COVID-19_CasesReported_5-21_5pm.csv')

df1=data['Total Cases'].str.split(': ',expand=True,n=1)

data['Total Cases']=df1[1]

citylist=data['Community'].tolist()

from geopy.geocoders import Nominatim
geolocator = Nominatim()
lat=[]
long_=[]
for city in citylist:
  country ="US"
  loc = geolocator.geocode(city+','+'New York,'+ country)
  if loc==None:
    lat.append(0)
    long_.append(0)
  else:
    lat.append(loc.latitude)
    long_.append(loc.longitude)

data['Latitude']=lat

data['Longitude']=long_

# Find FIPS code by lat and long
from urllib.request import Request, urlopen
FIPS_code=[]
for la, lo in zip(lat,long_):
  url = "https://geo.fcc.gov/api/census/block/find?latitude=" + str(la) + "&longitude="+ str(lo) +"&format=xml"
  request = Request(url)
  html = urlopen(request)
  da = html.read()
  da = str(da)
  start = da.find('FIPS')
  FIPS_code.append(da[start+6:start+21])

data['FIPS']=FIPS_code

data[data.FIPS=='null" bbox="nul']

data.drop([9,56])

data[data['Community'].duplicated()==True]

a=int(data['Total Cases'][38])+int(data['Total Cases'][39])

data['Total Cases'][38]=a

b=int(data['Total Cases'][104])+int(data['Total Cases'][105])+int(data['Total Cases'][106])

data['Total Cases'][104]=b

data=data.drop([39,105,106])

data

data['Total Cases']=data['Total Cases'].astype('int64')

data.dtypes

data.to_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/Nassaucounty_COVID-19_CasesReported_5-21_5pm.csv')

data = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/Suffolkcounty_COVID-19_CasesReported_5-22_1pm.csv')

data

citylist=data['1'].tolist()

from geopy.geocoders import Nominatim
geolocator = Nominatim()
lat=[]
long_=[]
for city in citylist:
  country ="US"
  loc = geolocator.geocode(city+','+'New York,'+ country)
  if loc==None:
    lat.append(0)
    long_.append(0)
  else:
    lat.append(loc.latitude)
    long_.append(loc.longitude)

data['Latitude']=lat
data['Longitude']=long_

# Find FIPS code by lat and long
from urllib.request import Request, urlopen
FIPS_code=[]
for la, lo in zip(lat,long_):
  url = "https://geo.fcc.gov/api/census/block/find?latitude=" + str(la) + "&longitude="+ str(lo) +"&format=xml"
  request = Request(url)
  html = urlopen(request)
  da = html.read()
  da = str(da)
  start = da.find('FIPS')
  FIPS_code.append(da[start+6:start+21])

data['FIPS']=FIPS_code

data[data.FIPS=='null" bbox="nul']

citylist=['Lake Grove','East Hampton','Quioque','Mastic','Oak Beach','Southampton']
lat=[]
long_=[]
for city in citylist:
  country ="US"
  loc = geolocator.geocode(city+','+'New York,'+ country)
  if loc==None:
    lat.append(0)
    long_.append(0)
  else:
    lat.append(loc.latitude)
    long_.append(loc.longitude)

data['Latitude'][53]=lat[0]
data['Latitude'][110]=lat[1]
data['Latitude'][131]=lat[2]
data['Latitude'][135]=lat[3]
data['Latitude'][147]=lat[4]
data['Latitude'][149]=lat[5]

data['Longitude'][53]=long_[0]
data['Longitude'][110]=long_[1]
data['Longitude'][131]=long_[2]
data['Longitude'][135]=long_[3]
data['Longitude'][147]=long_[4]
data['Longitude'][149]=long_[5]

# Find FIPS code by lat and long
from urllib.request import Request, urlopen
FIPS_code=[]
for la, lo in zip(lat,long_):
  url = "https://geo.fcc.gov/api/census/block/find?latitude=" + str(la) + "&longitude="+ str(lo) +"&format=xml"
  request = Request(url)
  html = urlopen(request)
  da = html.read()
  da = str(da)
  start = da.find('FIPS')
  FIPS_code.append(da[start+6:start+21])

data['FIPS'][53]=FIPS_code[0]
data['FIPS'][110]=FIPS_code[1]
data['FIPS'][131]=FIPS_code[2]
data['FIPS'][135]=FIPS_code[3]
data['FIPS'][147]=FIPS_code[4]
data['FIPS'][149]=FIPS_code[5]

data['3']=data['1']

data['1']=data['0']

data['0']=data['3']

data.drop(columns=['3'])

data['cases/1k']=data['2']

data=data.drop(columns=['3'])

data=data.drop(columns=['2'])

data=data.rename(columns={'0':'Community','1':'Total Cases'})

data['Total Cases']=data.loc[:,'Total Cases'].apply(lambda x: float(x.replace(",", "")))

data['Total Cases']=data['Total Cases'].astype('int64')

data.dtypes

data.head()

data.to_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/Suffolkcounty_COVID-19_CasesReported_5-22_1pm.csv')

data = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/Suffolkcounty_COVID-19_CasesReported_5-24_1pm.csv')
data['Latitude']=la
data['Longitude']=lo
data['FIPS']=fip
data['3']=data['1']
data['1']=data['0']
data['0']=data['3']
data.drop(columns=['3'])
data['cases/1k']=data['2']
data=data.drop(columns=['3'])
data=data.drop(columns=['2'])
data=data.rename(columns={'0':'Community','1':'Total Cases'})
data['Total Cases']=data.loc[:,'Total Cases'].apply(lambda x: float(x.replace(",", "")))
data['Total Cases']=data['Total Cases'].astype('int64')
data.to_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/Suffolkcounty_COVID-19_CasesReported_5-24_1pm.csv')
import plotly.express as px
mapbox_access_token = 'pk.eyJ1IjoiZmlzaGVlcCIsImEiOiJjazgwcXd5amIwMnRtM2ZwNDR5OHRjb2Q1In0.wUN67xk4G_3OYy9-tqoqgA'
px.set_mapbox_access_token(mapbox_access_token)
fig = px.scatter_mapbox(data, lat='Latitude', lon='Longitude',  color='Total Cases', size='Total Cases',
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=40, zoom=8,
                  hover_data=['Community', 'Total Cases'],width=1800, height=1000)
fig.show()

data=pd.read_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/Nassaucounty_COVID-19_CasesReported_5-23_9am.csv')

data1=pd.read_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/Suffolkcounty_COVID-19_CasesReported_5-23_1pm.csv')

data2=pd.concat([data,data1])

data2=data2.drop(columns=['Unnamed: 0'])

data2=data2.drop(columns=['Unnamed: 0.1'])

data2

data2.to_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/longisland_COVID-19_CasesReported_5-23.csv')

from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
data2 = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/longisland_COVID-19_CasesReported_5-23.csv')

import plotly.graph_objects as go
import plotly.express as px

mapbox_access_token ='pk.eyJ1IjoidC1nZyIsImEiOiJja2JhMWIxdmcwam02MnJ1ZnhwYTZrMGQ4In0.ud6xFjCcWm0mRoIC2n59-g'
px.set_mapbox_access_token(mapbox_access_token)
fig = px.scatter_mapbox(data2, lat='Latitude', lon='Longitude',  color='Total Cases', size='Total Cases',
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=40, zoom=8, mapbox_style='streets',
                  hover_data=['Community', 'Total Cases'],width=1800, height=1000,title = 'Long Island Covid-19 Confirmed Case(5-23)')
fig.show()

data = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/LI_covid19.csv')
data

citylist=data['Community'].tolist()

from geopy.geocoders import Nominatim
geolocator = Nominatim()
lat=[]
long_=[]
for city in citylist:
  country ="US"
  loc = geolocator.geocode(city+','+'New York,'+ country)
  if loc==None:
    lat.append(0)
    long_.append(0)
  else:
    lat.append(loc.latitude)
    long_.append(loc.longitude)

data['Latitude']=lat
data['Longitude']=long_
data[data['Latitude']==0]
citylist=['East Hampton','Lake Grove','Oak Beach','Mastic','Quioque','Southampton']
lat=[]
long_=[]
for city in citylist:
  country ="US"
  loc = geolocator.geocode(city+','+'New York,'+ country)
  if loc==None:
    lat.append(0)
    long_.append(0)
  else:
    lat.append(loc.latitude)
    long_.append(loc.longitude)
data['Latitude'][50]=lat[0]
data['Latitude'][123]=lat[1]
data['Latitude'][190]=lat[2]
data['Latitude'][209]=lat[3]
data['Latitude'][215]=lat[4]
data['Latitude'][246]=lat[5]
data['Longitude'][50]=long_[0]
data['Longitude'][123]=long_[1]
data['Longitude'][190]=long_[2]
data['Longitude'][209]=long_[3]
data['Longitude'][215]=long_[4]
data['Longitude'][246]=long_[5]
data['Latitude'][178]=40.704200
data['Longitude'][178]=-73.468918



data.to_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/LI_COVID-19_CasesReported_7_17.csv')

import plotly.graph_objects as go
import plotly.express as px

data2 = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Covid-19/LI_COVID-19_CasesReported_7_17.csv')
data2['7/17/20']=data2.loc[:,'7/17/20'].apply(lambda x: float(x.replace(",", "")))
data2['7/17/20']=data2['7/17/20'].astype('int64')
mapbox_access_token ='pk.eyJ1IjoidC1nZyIsImEiOiJja2JhMWIxdmcwam02MnJ1ZnhwYTZrMGQ4In0.ud6xFjCcWm0mRoIC2n59-g'
px.set_mapbox_access_token(mapbox_access_token)
fig = px.scatter_mapbox(data2, lat='Latitude', lon='Longitude',  color='7/17/20', size='7/17/20',
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=40, zoom=8, mapbox_style='streets',
                  hover_data=['Community', '7/17/20'],width=1800, height=1000,title = 'Long Island Covid-19 Confirmed Case(7-17)')
fig.show()

