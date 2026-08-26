#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
df = pd.read_csv(prefix+'yellow_tripdata_2021-01.csv.gz', nrows=100)

df.head()

df.dtypes

df.shape


# In[4]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    nrows=100,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[5]:


from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')


# In[7]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[12]:


df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[16]:


df_iter = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz',
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000)


# In[11]:


for df_chunk in df_iter:
    print(len(df_chunk))
    df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')


# In[17]:


from tqdm.auto import tqdm


first = True

for df_chunk in tqdm(df_iter):
# for df_chunk in df_iter:
    if first:
        df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')
        first = False
        print('Table created')
    df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
    print('Inserted: ', len(df_chunk))


# In[ ]:




