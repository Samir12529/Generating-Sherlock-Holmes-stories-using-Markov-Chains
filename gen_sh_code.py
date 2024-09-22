# Tools to use
import numpy as np
import pandas as pd
import os
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random


# "Fetching" the dataset
path = "C:\sherlock-holmes-stories\sherlock\sherlock/"
def read_ds(path):
    text = []
    for _, _, files in os.walk(path):
        for one_file in files:
            with open(path+one_file) as f:
                for l in f:
                    l = l.strip()
                    if l=='----------': break
                    if l!='':text.append(l)
    return text
        
raw_data = read_ds(path)


# Data cleansing
def clean_ds(text):
    cleaned_ds = []
    for l in text:
        l = l.lower()
        l = re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-\\]", "", l)
        tokens = word_tokenize(l)
        words = [word for word in tokens if word.isalpha()]
        cleaned_ds+=words
    return cleaned_ds

cleaned_data = clean_ds(raw_data)



# Create markov model
def create_markov_model(cleaned_data, n_w=2):
    markov_model = {}
    for i in range(len(cleaned_data)-n_w-1):
        curr_state, next_state = "", ""
        for j in range(n_w):
            curr_state += cleaned_data[i+j] + " "
            next_state += cleaned_data[i+j+n_w] + " "
        curr_state = curr_state[:-1]
        next_state = next_state[:-1]
        if curr_state not in markov_model:
            markov_model[curr_state] = {}
            markov_model[curr_state][next_state] = 1
        else:
            if next_state in markov_model[curr_state]:
                markov_model[curr_state][next_state] += 1
            else:
                markov_model[curr_state][next_state] = 1
    
    # calculating transition probabilities
    for curr_state, road in markov_model.items():
        total = sum(road.values())
        for state, count in road.items():
            markov_model[curr_state][state] = count/total
    return markov_model

markov_model = create_markov_model(cleaned_data)



# Generating Sherlock Holmes Stories
def generate_data(markov_model, limit=100, start='my god'):
    n = 0
    curr_state = start
    next_state = None
    end_data = ""
    end_data+=curr_state+" "
    while n<limit:
        next_state = random.choices(list(markov_model[curr_state].keys()),
                                    list(markov_model[curr_state].values()))
        
        curr_state = next_state[0]
        end_data+=curr_state+" "
        n+=1
    return end_data

for i in range(8):
    print(str(i)+". ", generate_data(markov_model, start="my dear", limit=8))