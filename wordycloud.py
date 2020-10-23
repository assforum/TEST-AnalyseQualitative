#!/usr/bin/env python
# Importing modules
import pandas as pd
import os
# Load the regular expression library
import re
import matplotlib.pyplot as plt

# Read data into papers
paper = pd.read_csv('papers.csv')

# Remove the columns
papers = paper.drop(columns=['id', 'event_type', 'pdf_name'], axis=1)
# Print out the first rows of papers
papers.head()

# Remove punctuation
papers['paper_text_processed'] = papers['paper_text'].map(lambda x: re.sub('[,\.!?]', '', x))
# Convert the titles to lowercase
papers['paper_text_processed'] = papers['paper_text_processed'].map(lambda x: x.lower())
# Print out the first rows of papers
papers['paper_text_processed'].head()
# Import the wordcloud library
from wordcloud import WordCloud
# Join the different processed titles together.
long_string = ','.join(list(papers['paper_text_processed'].values))
# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
# Generate a word cloud
wordcloud.generate(long_string)
# Visualize the word cloud
wordcloud.to_image()
# make figure to plot
plt.figure()
# plot words
plt.imshow(wordcloud, interpolation="bilinear")
# remove axes
plt.axis("off")
# show the result
plt.savefig('my_plot.png')
plt.show()