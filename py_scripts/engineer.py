# Visualisations for Data
import matplotlib.pyplot as plt
import seaborn as sns
import mining_hq
from numpy import count_nonzero

sns.set()
plt.xticks(rotation = 90)

games_pre = mining_hq.games_sales_split_pre
games_dur = mining_hq.games_sales_split_dur
games_pos = mining_hq.games_sales_split_pos

games_fig_pre = sns.barplot(data = games_pre, x = "Year", y = "NA_Sales", estimator = count_nonzero)
plt.show()

plt.xticks(rotation = 90)
games_fig_dur = sns.barplot(data = games_dur, x = "Year", y = "NA_Sales", estimator = count_nonzero)
plt.show()

plt.xticks(rotation = 90)
games_fig_pos = sns.barplot(data = games_pos, x = "Year", y = "NA_Sales", estimator = count_nonzero)
plt.show()
