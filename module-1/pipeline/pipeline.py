#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pandas as pd

day = sys.argv[1]
print(f"Running pipeline for day: {day}") 

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df.to_parquet(f'output_day_{sys.argv[1]}.parquet', engine='pyarrow', index=False)

