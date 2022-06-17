# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import snowflake.connector
import credentials


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

conn = snowflake.connector.connect(user=credentials.user, password=credentials.password, account=credentials.account)
curr = conn.cursor()

curr.execute("use role sysadmin")
print("Using role sysadmin")

curr.execute(f"use database {credentials.db}")
print(f"Using database {credentials.db}")

curr.execute(f"use warehouse {credentials.wh}")
print(f"Using {credentials.wh} warehouse")


res = curr.execute("select * from weather")

df = pd.DataFrame.from_records(iter(curr), columns=[x[0] for x in curr.description])

import pprint
pprint.pprint(df)

fig = px.line(df.tail(10), x="EVENTDATE", y="TEMP")

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='WEATHER STATION'),

    html.Div(children='''
        Visualization of python based weather app using Open Weather API connected to Snowflake. 
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

while True:
    print("yo")
    res = curr.execute("select * from weather")
    df = pd.DataFrame.from_records(iter(curr), columns=[x[0] for x in curr.description])
    fig = px.line(df.tail(10), x="EVENTDATE", y="TEMP")