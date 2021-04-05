# Stevie Dickerson - Math 543, Midterm Problem 2

#I, Stevie Dickerson, pledge that this program is completely my own work, and that I did not take, borrow or steal code from any other person, and that I did not allow any other person to use, have, borrow or steal portions of my code. I understand that if I violate this honesty pledge, I am subject to disciplinary action pursuant to the appropriate sections of the San Diego State University Policies.

import numpy as np
from numpy import linalg as la
from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
urlretrieve(url, 'covid.csv')

covid_data = pd.read_csv('covid.csv')
covid_data_US = covid_data.drop(['Province/State', 'Lat', 'Long'], axis=1, inplace=True)
covid_US = covid_data[covid_data['Country/Region'] == 'US'].T # Extract US data
covid_US = covid_US.iloc[1:]
recent_US = covid_US.iloc[-22:]
print(covid_US)
print(recent_US)

covid_US.plot(kind='bar')
recent_US.plot(kind='bar')

plt.show()