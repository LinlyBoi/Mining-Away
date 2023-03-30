# Visualisations for Data
import matplotlib.pyplot as plt
import seaborn as sns
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
games_fig2_pre = sns.histplot(data = games_pre, x = "Year", hue = "Genre", multiple = "stack", shrink = 0.65)
plt.show()

plt.xticks(rotation = 90)
games_fig_dur = sns.barplot(data = games_dur, x = "Year", y = "NA_Sales")
plt.xlabel("Years")
plt.ylabel("Sales in North America (Canada, USA)")
plt.show()

plt.xticks(rotation = 90)
games_fig_pos = sns.barplot(data = games_pos, x = "Year", y = "NA_Sales")
plt.show()

plt.xticks(rotation = 90)
crime_CA_fig = sns.barplot(data = crime_CA, x = "year", y = "incidents", estimator=count_nonzero)
plt.show()
