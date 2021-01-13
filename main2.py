import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_excel("C:/Users/com/Documents/Python Scripts/매출내역.xlsx")
df.columns = ["no","주문일","업체명","구분","매출액","입금액","입금일","세금계산","카드","현금영수증","담당번호","주문내역","받는분","주소", "문자발송 H.P","송장번호","구비서류","담당자","비고","비고2","비고3"]
df2 = pd.read_excel("C:/Users/com/Documents/Python Scripts/월별매출액.xlsx")
df2.columns = ["월","월별매출액"]




app.layout = html.Div([
    dcc.Dropdown(
        id="ticker",
        value = 'section',
        options=[{"label": x, "value": x} for x in ["사이트별 매출액", "자주가는 고객", "월별 매출액"]],
        clearable= False
    ),
    dcc.Graph(id="display_time_chart"),
    dcc.Graph(id="display_time_chart2")
])


@app.callback(
    Output("display_time_chart", "figure"), 
    [Input("ticker","value")])
def display_time_series(value):
    df["구분"].dropna()
    df["매출액"].dropna()
    flg = px.pie(data_frame=df, names = '구분',values ="매출액",title = "사이트별 매출액")
    return flg

@app.callback(
    Output("display_time_chart2", "figure"), 
    [Input("ticker","value")])
def display_month(value):

    flg = px.line(data_frame=df2.dropna(),x=df2["월"].dropna(),y=df2["월별매출액"].dropna(),
    labels =dict(x= "월" , y = "월별매출액",color = "월별매출액"),
    title = "월별매출액")

    flg.add_bar(x=df2["월"],y=df2["월별매출액"],name="월")

    flg.add_trace(go.Scatter(x=df2["월"],y = df2["월별매출액"],
    mode="lines+markers",
    name = "매출액"))
    return flg


        
   

app.run_server(debug=True)