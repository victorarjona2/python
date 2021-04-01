"""
    I, Victor Arjona, pledge that this program is completely my own work, and that I did not
    take, borrow or steal code from any other person, and that I did not allow any other person to
    use, have, borrow or steal portions of my code. I understand that if I violate this honesty
    pledge, I am subject to disciplinary action pursuant to the appropriate sections of the San
    Diego State University Policies.
"""

import numpy as np
from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

print_head = False
n = 50

# Problem 2f
#   Generate CSV to turn to Pandas DataFrame
url = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
urlretrieve(url, 'covid.csv')

#   Clean Data!
#       Useful labels to locate rows/columns
c_r = "Country/Region"
p_s = "Province/State"
lat = "Lat"
lon = "Long"

#       Turn CSV to Pandas Dataframe and extract the row for US. Drop all other columns. Clean
#       DataFrame. Read CSV.
df = pd.read_csv('covid.csv')

#       Isolate row for US and drop all columns except for the dates. Tranpose it. This turns the dates
#       into the index! We don't want that. Will be dealt with later.
df_us = df.loc[df[c_r] == "US", :].drop(columns=[c_r, p_s, lat, lon]).T

#       Change column from 249 to 'qty'
df_us = df_us.rename(columns={249: "qty"})

#       Make "unit" column.
df_us['unit_qty'] = df_us["qty"]/df_us["qty"].max()

#       Add dates (which is the current index) as a column.
df_us["date"] = df_us.index

#       Make index go from 0 to length of DataFrame. Doing this creates a new column called "index"
#       which is the same as the dates.
df_us = df_us.reset_index()

#       Remove index column.
df_us = df_us.drop(columns=["index"])

#       Turn "date" column, currently strings, to a DateTime.
df_us["date"] = pd.to_datetime(df_us["date"])

#       Get diff of total cases so we can get the number of new cases per day.
#       It'll be one element size less than df_us.
df_us_diff = pd.DataFrame({"date": df_us["date"][1:],
                          "diff_qty": np.diff(df_us["qty"])})

#       Debbuging: Clean data!
if print_head:
    print(df_us_diff.head())

#   2fi - Plot bar graph of new confirmed cases since 22JAN2020 - Present
fig, ax = plt.subplots(figsize=(7, 5))
plt.xlabel("Date")
plt.ylabel("QTY of new cases")
plt.title("New COVID cases per day since 22JAN2020 - Present")
ax.xaxis.set_major_locator(mdates.MonthLocator())
fmt = mdates.DateFormatter("%b %Y")
ax.xaxis.set_major_formatter(fmt)
ax.bar(df_us_diff["date"],
       df_us_diff["diff_qty"],
       width=0.5,
       align="center")

plt.setp(ax.get_xticklabels(), rotation=30)

#   2fii - Plot the linear regression of the last n data points onto the bar graph.
#       Isolate the last 22 data points.
df_us_last_n_diff = df_us_diff[-n:]

#       Do a linear regression on it. This gives us the slope and y-intercept.
[m, b] = np.polyfit(df_us_last_n_diff.index,
                    df_us_last_n_diff['diff_qty'],
                    1)

#       Make variables with the slope and y-intercept in scientific notation, 2 digits.
m_sci = np.format_float_scientific(m, precision=2)
b_sci = np.format_float_scientific(b, precision=2)

#       Generate values to plot.
lin_reg_vals = df_us_last_n_diff.index*m + b

#       Plot linear regression of last n.
ax.plot(df_us_last_n_diff["date"],
        lin_reg_vals,
        'ro--',
        linewidth=2,
        ms=2,
        label="Linear regression of 50 last days\n$y = mx + b$\n$m = {}$\n$b = {}$".format(m_sci, b_sci))

#   2fiii - Plot extrapolation of linear regression after the current date.
#       Supposed end date.
t_days_until_all_over_val = -b/m - df_us_last_n_diff.index[-1]
t_days_until_all_over_val_rounded = int(np.ceil(t_days_until_all_over_val))

#       Make new end of the linear regression of the graph.
#           Make new DataFrame with date starting at the end-date and ending at end-date plus
#           "t_days_until_all_over_rounded".
mid = df_us_last_n_diff.index[-1]
stop = mid + t_days_until_all_over_val_rounded

base = df_us_last_n_diff["date"][df_us_last_n_diff.index[-1]]
prediction_dates = pd.DataFrame({"pred_dates": [base + datetime.timedelta(days=ii) for ii in range(t_days_until_all_over_val_rounded)]})
prediction_dates = prediction_dates.set_index(pd.Index(np.arange(mid, mid + t_days_until_all_over_val_rounded)))

area_under_curve = float(0.5*(t_days_until_all_over_val)*df_us_last_n_diff["diff_qty"].tail(1))
area_under_curve = np.format_float_scientific(area_under_curve, precision=2)

lbl = "Linear regression of future until assumed last day.\nNumber of additional days is about {}.\nTotal new cases predicted to be {}"
lin_reg_vals = prediction_dates.index*m + b
ax.plot(prediction_dates["pred_dates"],
        lin_reg_vals,
        'gx--',
        linewidth=2,
        ms=2,
        label=lbl.format(t_days_until_all_over_val_rounded,
                         area_under_curve))

plt.legend()
plt.grid()
plt.tight_layout()
