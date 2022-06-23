import pandas as pd
import plotly.express as px

data = pd.read_csv('/Users/drpoojayadav/Downloads/Project 103/data.csv')

data_scatter = px.scatter(data, x = "date", y = "cases", color = "country", size = "cases",  hover_data = ['country', 'cases'], title = "COVID cases by country" )
data_scatter.show()
