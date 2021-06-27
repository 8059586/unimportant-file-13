import pandas as pd
import plotly.express as px
#reading the file
df = pd.read_csv("data.csv")
# graph to visualize data
fig = px.bar(df,x="Country",y="InternetUsers")
fig.show()