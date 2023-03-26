# Visualisations for Data
import seaborn as sns
import gunner

games_vis = gunner.game_sales_NA

sns.relplot(data = games_vis, x = "Year", y = "NA_Sales")
