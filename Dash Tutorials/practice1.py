from dash import Dash,dcc,html,dash_table,Output,Input
import pandas as pd    
import plotly.graph_objects as go  
import plotly.express as px

app = Dash(__name__)

data=pd.read_csv('snake_bite_data.csv')
data.columns=data.columns.str.strip().str.capitalize()
data['Date']=pd.to_datetime(data['Date'])

app.layout = html.Div([
    html.H2('Snake Bites in US'),
    html.Div([
        dcc.Dropdown(options=['Gender','Name'],value='',id='dropdown'),
        dcc.Graph(figure={},id='output')
    ]),
    dash_table.DataTable(data=data[['Name','Age','Gender','Species','Latitude','Longitude']].to_dict('records'),page_size=5)
])

@app.callback(
    Output('output','figure'),
    Input('dropdown','value')
)

def cols_chosen(inputs):
    fig = px.bar(data_frame=data,x=inputs,y='Age')
    return fig

app.run_server()