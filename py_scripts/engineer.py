# Visualisations for Data
import matplotlib.pyplot as plt
import seaborn as sns
import gunner
from numpy import count_nonzero

sns.set()
plt.xticks(rotation = 90)

games_pre = gunner.game_sales_NA_pre
games_dur = gunner.game_sales_NA_dur
games_pos = gunner.game_sales_NA_pos

games_fig_pre = sns.barplot(data = games_pre, x = "Year", y = "NA_Sales", estimator = count_nonzero)
plt.show()

plt.xticks(rotation = 90)
games_fig_dur = sns.barplot(data = games_dur, x = "Year", y = "NA_Sales", estimator = count_nonzero)
plt.show()

plt.xticks(rotation = 90)
games_fig_pos = sns.barplot(data = games_pos, x = "Year", y = "NA_Sales", estimator = count_nonzero)
plt.show()
