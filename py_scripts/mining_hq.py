# Instantiating Main Python Script File
# Collects stuff from the rest of the scripts
import pandas as pd
import numpy as np
import seaborn as sns
import digger

import pandas as pd
from tkinter.filedialog import askopenfilename

games_review = pd.read_csv("datasets/videogames/Games.xls")
games_sales = pd.read_csv("datasets/videogames/vgsales-12-4-2019-short.csv")

games_review_phase1 = digger.slice_column(games_review, "GameName", "Review")
games_review_final = digger.slice_column(games_review, "GameName", "(Import)")
games_merged_dat = digger.write_joined_df(games_sales, games_review_final)
games_merged_dat.to_csv("datasets/videogames/games_merged.csv")
