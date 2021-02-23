import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv('studentappdata.csv')

plot = px.scatter( 
df,
x = df.groupby('level')['attempt'].mean(),
y = ['level 1', 'level 2', 'level 3', 'level 4'],
color='level',
size='attempt'
)

plot.show()


