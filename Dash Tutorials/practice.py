from dash import Dash,dcc,html,Input,Output,State

app = Dash(__name__)

app.layout = html.Div([
    html.H2('Text Classification'),
    dcc.Input(id='input',placeholder='Enter text for sentiment analysis....',value='',type='text'),
    html.Button(id='button',n_clicks=0,children='Predict'),
    html.P(id='output',children='')
])

@app.callback(
    Output('output','children'),
    Input('button','n_clicks'),
    State('input','value')
)

def output(n_clicks,prompt):
    if prompt:
        result=len(prompt)
        return result 
    
app.run_server()

