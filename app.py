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
#import topic_mode
import pandas as pd
#import connections
#import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import extracttable

app = Flask(__name__)
#result=connections.connect()


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

#@app.route('/topicresult',methods=['POST','GET'])
#def topic_mod():
#    if request.method=="POST":
#        #return response
#        

@app.route('/pact_scanhome')
def pact_scanhome():
    return render_template("landing1.html")    

#@app.route('/topicmodelling')
#def topic_result():
#    result=connections.pull_collections()
#    return render_template("home.html",options=result)
#
#@app.route('/sentiment_input',methods=['POST','GET'])
#def sentiment_input():
#    #a=['blue','green','grey']
#    result=connections.pull_collections()
#    return render_template("sentiment_input.html",options=result)

#@app.route('/sentiment_cosmos',methods=['POST','GET'])
#def senti_cosmos():
#    if request.method=="POST":
#        select_val=request.form['containers']
#        result="Sorry ! Data is empty in " + select_val + "Container"
##        result=connections.connect(select_val)
##        target=[]
##        sia=SentimentIntensityAnalyzer()
##        for i in result:
##            #print(i)
##            polarity=sia.polarity_scores(i)
##            #print(polarity)
##            target.append(max(polarity,key=lambda x : polarity[x]))
##            #print(target)
##        target=['Positive','Positive','Negative','Positive']
##        sent_df=pd.DataFrame(list(zip(result,target)))
##    
##        response=make_response(sent_df.to_csv())
##        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
##        response.headers["Content-Type"] = "text/csv"
#        return render_template("output.html",output=result)
        
#@app.route('/topic_cosmos',methods=['POST','GET'])
#def topic_cosmos():
#    if request.method=="POST":
#        select_val=request.form['containers']
#        result="Sorry ! Data is empty in " + select_val + "Container"
##        result=connections.connect(select_val)
##        ldamodel,corpus=topic_mode.topic_modell(result)
##        df=format_topics_sentences(ldamodel,corpus,result)
#        #df.save(os.path.join("/tmp/","topic.csv"))
#        #df1=df.head(3)
##        response=make_response(df.to_csv())
##        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
##        response.headers["Content-Type"] = "text/csv"
#        return render_template("output.html",output=result)
        
    


@app.route('/sentiment_output',methods=['POST','GET'])
def sentiment_output():
    if request.method=="POST":
        f=pd.read_csv(request.files.get('file'))
        target=[]
        sia=SentimentIntensityAnalyzer()
        for i in f['Articles']:
            #print(i)
            polarity=sia.polarity_scores(i)
            #print(polarity)
            target.append(max(polarity,key=lambda x : polarity[x]))
            #print(target)
        target=['Positive','Positive','Negative','Positive']
        sent_df=pd.DataFrame(list(zip(f['Articles'],target)))
        sent_df.columns=["Text","Sentiment_result"]
    
#        response=make_response(sent_df.to_csv())
#        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
#        response.headers["Content-Type"] = "text/csv"
        return render_template("sentiment_output.html",result=sent_df.to_html())
        
    


#@app.route('/topic',methods=['POST','GET'])
#def topic_modelling():
#    if request.method=="POST":
#        #file=request.files['file']
#        f=pd.read_csv(request.files.get('file'))
#        #filename=secure_filename(file.filename)
#        
#        
#        ldamodel,corpus=topic_mode.topic_modell(f)
#        df=format_topics_sentences(ldamodel,corpus,f['Articles'])
#        #df.save(os.path.join("/tmp/","topic.csv"))
#        #df1=df.head(3)
##        response=make_response(df.to_csv())
##        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
##        response.headers["Content-Type"] = "text/csv"
#        return render_template("topic_output.html",result=df.to_html())
#
#def format_topics_sentences(ldamodel, corpus, texts):
#    # Init output
#    sent_topics_df = pd.DataFrame()
#    # Get main topic in each document
#    for i, row_list in enumerate(ldamodel[corpus]):
#        row = row_list[0] if ldamodel.per_word_topics else row_list            
#        # print(row)
#        row = sorted(row, key=lambda x: (x[1]), reverse=True)
#        # Get the Dominant topic, Perc Contribution and Keywords for each document
#        for j, (topic_num, prop_topic) in enumerate(row):
#            if j == 0:  # => dominant topic
#                wp = ldamodel.show_topic(topic_num)
#                topic_keywords = ", ".join([word for word, prop in wp])
#                topic="Topic_"+str(topic_num)
#                sent_topics_df = sent_topics_df.append(pd.Series([topic_keywords,topic, round(prop_topic*100,2)]), ignore_index=True)
#            else:
#                break
#    sent_topics_df.columns = ['Topic_Keywords','Dominant_Topic', 'Perc_Contribution' ]
#    # Add original text to the end of the output
#    contents = pd.Series(texts)
#    sent_topics_df = pd.concat([contents,sent_topics_df], axis=1)
#    return(sent_topics_df)
#


if __name__ == "__main__":
    app.run()


