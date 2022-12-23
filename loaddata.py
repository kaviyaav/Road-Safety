#!/usr/bin/env python
# coding: utf-8

# In[4]:


import psycopg2
from datetime import datetime
import pandas as pd
conn = psycopg2.connect( host="localhost",
    database="RoadSafety",
    user="postgres",
    password="Jolly@123")
cur = conn.cursor()
        
	# execute a statement
print('PostgreSQL database version:')
fields = ['accident_index', 'latitude', 'longitude', 'date', 'time', 'day_of_week', 'number_of_vehicles',
              'number_of_casualties']
df = pd.read_csv('C:/Users/raksh/Downloads/accident-data.csv', skipinitialspace=True, usecols=fields)

df['TimeStamp'] = df['date'] + ' ' + df['time']
for i in range(len(df['TimeStamp'])):
    df['TimeStamp'][i] = datetime.strptime(df['TimeStamp'][i], '%d/%m/%Y %H:%M').strftime('%Y-%m-%d %H:%M')


df = df[['accident_index', 'TimeStamp', 'latitude', 'longitude', 'number_of_vehicles', 'number_of_casualties',
             'day_of_week']]


df=df.fillna(0)
print(df['accident_index'][0])
sql = "INSERT INTO Accident VALUES (%s, %s,%s, %s,%s, %s,%s)"
for i in range(len(df['accident_index'])):
    val = (int(df['accident_index'][i]),float(df['latitude'][i]),float(df['longitude'][i]),int(df['number_of_vehicles'][i]),int(df['number_of_casualties'][i]),int(df['day_of_week'][i]),(df['TimeStamp'][i]))
    cur.execute(sql, val)
    conn.commit();


# In[5]:


import psycopg2
import pandas as pd

conn = psycopg2.connect( host="localhost",
database="RoadSafety",
user="postgres",
password="Jolly@123")
cur = conn.cursor()
fields = ['accident_index', 'urban_or_rural_area', 'road_type', 'road_surface_conditions', 'light_conditions',
          'weather_conditions', 'accident_severity']
df = pd.read_csv('C:/Users/raksh/Downloads/accident-data.csv', skipinitialspace=True, usecols=fields)

df = df[['accident_index', 'urban_or_rural_area', 'road_type', 'road_surface_conditions', 'light_conditions',
         'weather_conditions', 'accident_severity']]
print(pd.isnull(df['accident_severity']).sum())
sql = "INSERT INTO accidentdetails VALUES (%s, %s,%s,%s,%s,%s,%s)"
for i in range(len(df['accident_index'])):
    val = (int(df['accident_index'][i]),int(df['urban_or_rural_area'][i]),int(df['road_type'][i]),int(df['road_surface_conditions'][i]),int(df['light_conditions'][i]),
           int(df['weather_conditions'][i]),int(df['accident_severity'][i]))
    cur.execute(sql, val)
    conn.commit();   


# In[ ]:





# In[ ]:




