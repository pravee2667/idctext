# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

"""
    File Name       : pact.py
    Author          : P0142221
    Date Created    : 22-07-2019
    Date Modified   : 
    Python Version  : 3.6.5
    
"""

from nltk import pos_tag

import numpy as np
import re
#from wordcloud import WordCloud
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from flask import request
#def preprocessing(data):
#    data=data.lower()
#    data_feed=re.split(r'(Feedback: | Response)',data)[2]
#    data_feed1=re.sub('[\n]','',data_feed)
#    data_feed2=re.sub('[\r]','',data_feed1)
#    data_dig=re.sub('\d','',data_feed2)
#    data_pun=re.sub('[&#?;.()*.,]','',data_dig)
#    data_pun_w=re.sub(r'\b\w{1,3}\b','',data_pun)
#    data_pun_word=[f for f in data_pun_w.split(' ') if len(f)>0]
#    return data_pun_word



def clean(data):
    
    data=data.lower()
    #data_feed=re.split(r'(feedback:|response:)',data)[2]
    data_feed1=re.sub('[\n]','',data)
    data_feed2=re.sub('[\r]','',data_feed1)
    data_dig=re.sub('\d','',data_feed2)
    data_pun=re.sub('[&#?;.()*.,]','',data_dig)
    data_pun_w=re.sub(r'\b\w{1,3}\b','',data_pun)
    data_pun_word=[f for f in data_pun_w.split(' ') if len(f)>0]
#    #data_pos=pos_tag(data_pun_word)
#    text = [WordNetLemmatizer().lemmatize(t[0], tag_words_pos(t[1])) for t in data_pos]
#    text=" ".join(text)
    return data_pun_word
 

def tag_words_pos(items):
    if items.startswith("N"):
        return wordnet.NOUN
    elif items.startswith("J"):
        return wordnet.ADJ
    elif items.startswith("R"):
        return wordnet.ADV
    elif items.startswith("V"):
        return wordnet.VERB
    else:
        return wordnet.NOUN

def words(data):
    
    data['Fd_Clean']=data['Articles'].apply(lambda x : clean(x))
    return data['Fd_Clean']
    


    
#Frequent terms in bar plot
def freq_hist_plot(df):
    count_v=CountVectorizer()
    result_c=count_v.fit_transform(df['Feedback_cleaned']).toarray()
    fig, ax = plt.subplots(figsize=(16,8))
    ax.bar(range(len(count_v.get_feature_names())), result_c.sum(axis=0));
    ax.set_xticks(range(len(count_v.get_feature_names())));
    ax.set_xticklabels(count_v.get_feature_names(), rotation='vertical');
    ax.set_title('Top words in headlines dataset (excluding stop words)');
    ax.set_xlabel('Word');
    ax.set_ylabel('Number of occurences');
    plt.show()

    

    
# Context 
    
# Topic Modelling

