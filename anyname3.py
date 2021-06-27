import pandas as pd
import plotly.express as px
#reading the file
df = pd.read_csv("line_chart.csv")
# graph to visualize data
fig = px.line(df,x="Year",y="Per capita income",color="Country",title="Anytitle")
fig.show()