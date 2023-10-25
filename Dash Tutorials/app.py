from dash import Dash,dcc,html,Output,Input
import plotly.graph_objs as go
import pandas as pd

app=Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1(children='Dash App Tutorial'),
        html.Img(src='/assets/pixel.jpg'),
        html.Div([
            dcc.Input(
                id='input',
                value='',
                type='text'
            )
        ]),
        html.Div(
            dcc.Dropdown(
                options=[
                    {'label':'Candlestick','value':'Candlestick'},
                    {'label':'Line','value':'Line'}
                ]
                )),
        html.Div(
            dcc.Graph(
                id='chart'
            )
        )],className='banner')
    
])

@app.callback(
    Output('chart','figure'),
    Input('input','value')
)

def update_fig(input_value):
    data=pd.read_csv('snake_bite_data.csv')
    data['Date']=pd.to_datetime(data['Date'])
    file=[]
    plot=go.Scatter(x=data['Date'],y=data[' age'],name='scatter',line=dict(color='darkgreen'))
    file.append(plot)
    layout={'title':'Callback Graph'}
    return {
        'data':data,
        'layout':layout
    }
    
app.run()