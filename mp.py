import pandas as pd
import csv
import plotly.figure_factory as ff 

df = pd.read_csv("mobile_Phones.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Average ratings"],show_hist=False)
fig.show()