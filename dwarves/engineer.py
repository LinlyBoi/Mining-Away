# Visualisations for Data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import mining_hq
from numpy import count_nonzero

games_pre = mining_hq.games_sales_split_pre
games_dur = mining_hq.games_sales_split_dur
games_pos = mining_hq.games_sales_split_pos

crime_US = mining_hq.crime_US_intersect
crime_CA = mining_hq.crime_CA_intersect

custom_params = {"axes.spines.right": False, "axes.spines.top": False}

sns.set_theme(style = 'ticks', rc = custom_params)

plt.xticks(rotation = 90)
games_fig_pre = sns.histplot(data = games_pre, x = "Year", palette = sns.color_palette("flare"), kde = True)
plt.show()

plt.xticks(rotation = 90)
games_fig2_pre = sns.histplot(data = games_pre, x = "Year", hue = "Genre", multiple = "stack", kde = True)
plt.show()

plt.xticks(rotation = 90)
games_fig_dur = sns.histplot(data = games_dur, x = "Year", kde = True)
plt.show()

plt.xticks(rotation = 90)
games_fig2_dur = sns.histplot(data = games_dur, x = "Year", hue = "Genre", multiple = "stack", kde = True)
plt.show()

plt.xticks(rotation = 90)
games_fig3_dur = sns.jointplot(data = games_dur, x = "Year")
plt.show()

plt.xticks(rotation = 90)
games_fig_pos = sns.histplot(data = games_pos, x = "Year")
plt.show()

plt.xticks(rotation = 90)
crime_CA_fig = sns.barplot(data = crime_CA, x = "year", y = 'incident_sum')
plt.show()

plt.xticks(rotation = 90)
crime_US_fig = sns.barplot(data = crime_US, x = "report_year", y = "sum_violence")
plt.show()

games_dur['Violent_US'] = crime_US['violent_crimes']
games_dur['NA_Sales'] = games_dur['NA_Sales'].multiply(1000)

plt.xticks(rotation = 90)
games_violence_US = sns.relplot(data = games_dur, x = 'NA_Sales', y = 'Violent_US')
plt.close(1)
plt.show()

plt.xticks(rotation = 90)
games_crime_dur = sns.jointplot(data = games_dur, x = "Year", y = 'Violent_US')
plt.close(1)
plt.show()
