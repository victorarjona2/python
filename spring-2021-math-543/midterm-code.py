"""
    I, Victor Arjona, pledge that this program is completely my own work, and that I did not
    take, borrow or steal code from any other person, and that I did not allow any other person to
    use, have, borrow or steal portions of my code. I understand that if I violate this honesty
    pledge, I am subject to disciplinary action pursuant to the appropriate sections of the San
    Diego State University Policies.
"""

import numpy as np
from numpy import linalg as la
from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt

# Problem 2f
# Generate CSV to turn to Pandas DataFrame
url = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
urlretrieve(url, 'covid.csv')

# Useful labels to locate rows/columns
c_r = "Country/Region"
p_s = "Province/State"
lat = "Lat"
lon = "Long"

# Turn CSV to Pandas Dataframe and extract the row for US. Drop all other columns.
#   Read CSV.
df = pd.read_csv('covid.csv')

#   Isolate row for US and drop all collumns except for the dates.
#   "Unitize" everything.
#   Tranpose it. This turns the dates into the index!
df_us1 = df.loc[df[c_r] == "US", :].drop(columns=[c_r, p_s, lat, lon]).T
df_us1_max = df_us1.max()
df_us1 = df_us1/df_us1_max

# Generate a list of the
t_vals = pd.to_datetime(df_us1.index)

plt.plot(t_vals, df_us1)
#plt.bar(t_vals, df_us1)


#df_clean = df.drop(['Province/State', 'Lat', 'Long'], axis=1, inplace=True)
# covid_US = covid_data[covid_data['Country/Region'] == 'US'] # Extract US data
# print(covid_US)

# print(covid_data.shape)
# print(covid_data.head())
# print(covid_data.columns.values)

#days = []
#days = np.append(days, covid_US.columns.values[:-2]) # Append columns
# days = days[-22:]
# print(days)
#print(len(days))

# cases = []
# cases = np.arange(covid_US[1,len(days)]) # Append row
# print(cases)
# print(len(cases))

#covid_US.plot()

# fig = plt.figure(figsize=(7, 7))
# ax = plt.gca()
# df_US = df(covid_US, rows='US', columns=days)
# df[['US']].plot(kind='bar', x=days, y='US')
# ax.bar(x=days, y="US")
# plt.grid()
# plt.title("Plot Sum of Number of Cases per Day")
# plt.xlabel("Date")
# plt.ylabel("Total Cases")
#plt.show()
