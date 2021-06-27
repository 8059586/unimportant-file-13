import pandas as pd
import plotly.express as px
#reading the file
df = pd.read_csv("data.csv")
# graph to visualize data
fig = px.scatter(df,x="Population",y="Per capita",color="Country",size="Percentage")
fig.show()