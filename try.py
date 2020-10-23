#!/usr/bin/env python3


import nltk
from nltk import word_tokenize

text = "Google’s CEO Sundar Pichai introduced the new Pixel at Minnesota Roi Centre Event"

token = word_tokenize(text)
tags = nltk.pos_tag(token)
from nltk import ne_chunk

chunk = ne_chunk(tags)
import json
print (chunk)