#!/usr/bin/env python3

import os    
os.makedirs("thisfolder");

import nltk
from nltk import word_tokenize
from nltk import ne_chunk
import json
import numpy as np
import sys
import os
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
#!/usr/bin/env python
print("Hello World!")
#mandatory space at the end of the sentences
liste=["Cats are awesome ","Pacco is an amazing husky ","We can't give up on our projects ","we will be stronger in a few days "]


input=''.join(liste)
#Input
#input="Huskies are superb"




#Translate
# blob = TextBlob(input)
# lang=blob.detect_language()
# if(lang!=='en'):
    # blob.translate(from_lang=lang, to ='en')

#Tokenization
result=input.split(" ")
#create manually the output file beforehand
with open("C:/wamp64/www/TEST/output.txt", 'w') as f:
    for item in result:
        f.write("%s\n" % item)
        
        
#Generate wordcloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud
dataset = open("tags.txt", "r").read()
cloud = WordCloud().generate(dataset)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
plt.savefig("C:/wamp64/www/TEST/wordcloud"+".png", bbox_inches='tight')



#Positive vs negative
bloblist = list()
blob = TextBlob(input)

bloblist.append((input,blob.sentiment.polarity, blob.sentiment.subjectivity))

myListJson = json.dumps(bloblist) #Encode our Python list into a JSON string
f = open("C:/wamp64/www/TEST/tags.txt", "w") #Open the file that we want to write to for write access
f.write(myListJson) #Write the JSON String to the file that we have currently open
f.close() 
# Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. Subjective sentences generally refer to personal opinion, emotion or judgment whereas objective refers to factual information. Subjectivity is also a float which lies in the range of [0,1].


for x in range(len(liste)):
    resultat=liste[x].split(" ")
    with open("C:/wamp64/www/TEST/participants/outputs/output"+str(x)+".txt", 'w') as f:
        for item in resultat:
            f.write("%s\n" % item)
    #Generate wordcloud
    dataset = open("tags.txt", "r").read()
cloud = WordCloud().generate(dataset)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("C:/wamp64/www/TEST/participants/wordClouds/participant.png", bbox_inches='tight')

plt.tight_layout(pad=0)
plt.show()
    plt.close()
    wordcloudi=None
    #Positive vs negative
    bloblist2 = list()
    blob2 = TextBlob(liste[x])
    bloblist2.append((liste[x],round(blob2.sentiment.polarity, 1) , round(blob2.sentiment.subjectivity,1)))
    myListJson2 = json.dumps(bloblist2) #Encode our Python list into a JSON string
    f = open("C:/wamp64/www/TEST/participants/tags/tags"+str(x)+".txt", "w") #Open the file that we want to write to for write access
    f.write(myListJson2) #Write the JSON String to the file that we have currently open
    f.close() 








