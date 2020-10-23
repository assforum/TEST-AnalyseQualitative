#!/usr/bin/env python

import warnings
# Importing modules
import pandas as pd
import os
# Load the regular expression library
import re
import json
#print (json.dumps([[1,2,3], [2,4,6]]))
warnings.simplefilter("ignore", DeprecationWarning)
# Load the LDA model from sk-learn
from sklearn.decomposition import LatentDirichletAllocation as LDA
# Load the library with the CountVectorizer method
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 # Read data into papers
paper = pd.read_csv('papers.csv')

# Remove the columns
papers = paper.drop(columns=['id', 'event_type', 'pdf_name'], axis=1)
# Print out the first rows of papers
#print(papers.head())
#!/usr/bin/env python
# Remove punctuation
papers['paper_text_processed'] = papers['paper_text'].map(lambda x: re.sub('[,\.!?]', '', x))
# Convert the titles to lowercase
papers['paper_text_processed'] = papers['paper_text_processed'].map(lambda x: x.lower())
# Print out the first rows of papers
#print(papers['paper_text_processed'].head())
# Tweak the two parameters below
number_topics = 5
number_words = 10

#Create and fit the LDA model
count_vectorizer = CountVectorizer(stop_words='english')
#Fit and transform the processed titles
count_data = count_vectorizer.fit_transform(papers['paper_text_processed'])
lda = LDA(n_components=number_topics, n_jobs=-1)
lda.fit(count_data)
#Helper function
# def print_topics(model, count_vectorizer, n_top_words):
    # words = count_vectorizer.get_feature_names()
    # for topic_idx, topic in enumerate(model.components_):
        #print("\nTopic #%d:" % topic_idx)
        # " ".join([words[i]
                        # for i in topic.argsort()[:-n_top_words - 1:-1]])
        

words = count_vectorizer.get_feature_names()
for topic_idx, topic in enumerate(lda.components_):
    p=" ".join([words[i]
        for i in topic.argsort()[:-number_words - 1:-1]])
        
#Print the topics found by the LDA model
#print("Topics found via LDA:")
#p=print_topics(lda, count_vectorizer, number_words)
import json
print (json.dumps(p));