# Visualisations for Data
import matplotlib.pyplot as plt
import seaborn as sns
import gunner
from numpy import count_nonzero

sns.set()
plt.xticks(rotation=90)

games_vis = gunner.game_sales_NA

games_fig = sns.barplot(data = games_vis, x = games_vis["Year"], y = games_vis["NA_Sales"], estimator = count_nonzero)

plt.show()
