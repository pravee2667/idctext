# -*- coding: utf-8 -*-

import pre_process
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.feature_extraction.text import CountVectorizer
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

def topic_modell(data):
    clean_data=pre_process.words(data)
#    cv=CountVectorizer(min_df=0)
#    cv_transf=cv.fit_transform(clean_data.values)
#    lda = LDA(n_components=2, max_iter=5,
#                                learning_method = 'online',
#                                learning_offset = 50.,
#                                random_state = 0)
#    fnames=cv.get_feature_names()
#    lda.fit(cv_transf)
#    words=print_top_words(lda,fnames,5)
    dictionary = corpora.Dictionary(clean_data)
    corpus = [dictionary.doc2bow(text) for text in clean_data]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=dictionary,
                                           num_topics=2, 
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)
    return ldamodel,corpus
    
    





#
#def topic_modell(data):
#    clean_data=pre_process.words(data)
#    cv=CountVectorizer(min_df=0)
#    cv_transf=cv.fit_transform(clean_data.values)
#    lda = LDA(n_components=2, max_iter=5,
#                                learning_method = 'online',
#                                learning_offset = 50.,
#                                random_state = 0)
#    fnames=cv.get_feature_names()
#    lda.fit(cv_transf)
#    words=print_top_words(lda,fnames,5)
#    
#    return words
#    
#
#def print_top_words(model, feature_names, n_top_words):
#    word=[]
#    for index, topic in enumerate(model.components_):
#        message = "\nTopic #{}:".format(index)
#        message += " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1 :-1]])
#        word.append(message)
#    return word