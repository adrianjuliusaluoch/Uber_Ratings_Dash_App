#Import Dependecnies
from dash import Dash,html,dcc,Input,Output
from transformers import AutoTokenizer,AutoModelForSequenceClassification,pipeline

#Initialize Model
model_name='nlptown/bert-base-multilingual-uncased-sentiment'
nlp = pipeline("sentiment-analysis", model=model_name,tokenizer=model_name)

#App FrameWork
app=Dash(__name__)

app.layout=html.Div([
    html.H2('Uber Ratings'),
    dcc.Input(id='input',placeholder='Enter your review here....',value='',type='text',className='input'),
    html.P(id='output',children='')
],className='banner')

#Create a callback for inputs and outputs
@app.callback(
    Output('output','children'),
    Input('input','value')
)

def predict_sentiment(text):
    if text:
        predictions = nlp(text)
        sentiment = predictions[0]['label']
        confidence = predictions[0]['score']
        return f"{sentiment} : {confidence:.2f}"

app.run()