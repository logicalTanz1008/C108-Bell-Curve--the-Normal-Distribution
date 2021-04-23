import csv
import plotly.figure_factory as pf
import pandas as pd 

file = pd.read_csv("data.csv")
fileList = file["Avg Rating"].tolist()

fig = pf.create_distplot([fileList], ["Avg Rating"], show_hist=False)

fig.show()