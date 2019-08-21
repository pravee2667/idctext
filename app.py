# -*- coding: utf-8 -*-

#from flask import Flask,send_file,render_template,request,url_for,redirect
#import matplotlib.pyplot as plt
#from matplotlib.figure import Figure
#from io import BytesIO
#from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
#from bokeh.models import (HoverTool,FactorRange,Plot,LinearAxis,
#                          Grid,Range1d)
#from  bokeh.models.glyphs import VBar
#from bokeh.plotting import figure
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
##from bokeh.charts import Bar
#from werkzeug import secure_filename
#import topic_mode
#import pandas as pd
#from bokeh.embed import components
#from bokeh.models.sources import ColumnDataSource
#import connections
#app = Flask(__name__)
#
#result=connections.connect()
#
#@app.route('/home')
#def hello_world():
#    return render_template("home.html")
#
#@app.route('/',methods=['POST','GET'])
#def login():
#    error = None
#    if request.method=='POST':
#        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#            error = 'Invalid Credentials. Please try again.'
#        else:
#            return redirect(url_for('hello_world'))
#    return render_template('login.html', error=error)
#        
#        
#
#@app.route('/sentiment',methods=['POST','GET'])    
#def polarity():
#    if request.method=="POST":
#        messa=request.form['message']
#        #sia=SentimentIntensityAnalyzer()
#        #s_polarity=sia.polarity_scores(messa)
#        s_polarity={'neg': 0.192, 'neu': 0.411, 'pos': 0.397, 'compound': 0.3612}
#        return render_template("sentiment.html",result=s_polarity)
#
#@app.route('/topic',methods=['POST','GET'])
#def topic_modelling():
#    if request.method=="POST":
#        f=pd.read_csv(request.files.get('file'))
#        #ff=secure_filename(f.filename)
#        result=topic_mode.topic_modell(f)
#        return render_template("output.html",output=result)
#        
#        
#
#
#if __name__ == "__main__":
#    app.run()



from flask import Flask,send_file,render_template,request,url_for,redirect,make_response
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from werkzeug import secure_filename
#import pyLDAvis.gensim
import topic_mode
import pandas as pd
import connections

app = Flask(__name__)
result=connections.connect()


@app.route('/home')
def hello_world():
    return render_template("landing.html")

@app.route('/',methods=['POST','GET'])
def login():
    error = None
    if request.method=='POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('hello_world'))
    return render_template('login.html', error=error)

@app.route('/topicmodelling')
def topic_mod():
    return render_template("home.html")


@app.route('/topic',methods=['POST','GET'])
def topic_modelling():
    if request.method=="POST":
        f=pd.read_csv(request.files.get('file'))
        #ff=secure_filename(f.filename)
        ldamodel,corpus=topic_mode.topic_modell(f)
        df=format_topics_sentences(ldamodel,corpus,f['Articles'])
        response=make_response(df.to_csv())
        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
        response.headers["Content-Type"] = "text/csv"
        return response

def format_topics_sentences(ldamodel, corpus, texts):
    # Init output
    sent_topics_df = pd.DataFrame()
    # Get main topic in each document
    for i, row_list in enumerate(ldamodel[corpus]):
        row = row_list[0] if ldamodel.per_word_topics else row_list            
        # print(row)
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']
    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return(sent_topics_df)



if __name__ == "__main__":
    app.run()


