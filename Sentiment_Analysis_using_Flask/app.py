from flask import Flask,request,render_template,url_for

# Import SentimentIntensityAnalyzer And Flask 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#creating object for the SentimentIntensityAnalyzer Class
sid = SentimentIntensityAnalyzer()

#Declaring the name 
app = Flask(__name__)


#Main Program
@app.route('/',methods=["POST","GET"])
def predict():
    if request.method=='POST':
        string = request.form['sentence']
        
        if string == 'None' or string =="": #this statement is to handle null values
            return render_template('index.html',sentence = "Please enter a sentence")
        else:
            scores = sid.polarity_scores(string)
        
            if scores['compound'] == 0:
                sentiment = "Neutral"
            elif scores['compound'] > 0:
                sentiment = "Positive"
            else:
                sentiment = "Negative"
        return render_template('index.html',sentiment = sentiment,sentence = string)
    else:
    	result = "method invalid passed"
    	return render_template('index.html',result = result)


if __name__ == "__main__":
    app.run(debug=True)
