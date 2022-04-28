import pandas as pd
import numpy as np

#Load the data
df_2019 = pd.read_csv("2019-MA.csv")
df_2020 = pd.read_csv("2020-MA.csv")
df_2021 = pd.read_csv("2021-MA.csv")

#combining the df's to 1 df




#Cleaning and checking
#datetime, check for total days of data in a year, if all 0 then PROBLEM

#Check for days without rain, remove days with rain

#check for days with wind above 15 kt

#check for days with wind_gust above 20 kt

#check for days with wind of 15 kt AND gust_wind of 20
