##CTRL + SHIFT + B to run

#Importing Keras (ml framework)
import keras.utils as ku
#Keras layers
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
#Tokenizer
from keras.preprocessing.text import Tokenizer
#generating our model
from keras.models import Sequential
# To address overfitting
from keras.callbacks import EarlyStopping
# To enable sequencing in our data
from keras.preprocessing.sequence import pad_sequences
# Seeds for reproducibility
from tensorflow import set_random_seed
from numpy.random import seed
set_random_seed(2)
seed(1)
import re
import pandas as pd
import numpy as np
import string, os

lines = open('movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
conv_lines = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

lines[:10]

#Getting rid of unnecessary texts in data
id2line = {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]

convs = [ ]
for line in conv_lines[:-1]:
    _line = line.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    convs.append(_line.split(','))

#Append the split lines into sentences
conversations = []
for conv in convs:
    for i in range(len(conv)-1):
        conversations.append(id2line[conv[i]])

print(conversations[1])

for i in range(0,10):
  print(conversations[i])

# Declare a tokenizer object to use
tokenizer = Tokenizer()

def get_sequences(text):
    # encode our words
    tokenizer.fit_on_texts(text)
    # how many words we have in total ( + 1 because it starts at 0)
    total_words = len(tokenizer.word_index) + 1
    ## convert data to sequence
    sequences = []
    for sentence in text:
        token_sentences = tokenizer.texts_to_sequences([sentence])[0]
        for i in range(1, len(token_sentences)):
            # For each token (word) in our sentence we create an array with the token and its previous tokens
            sequence = token_sentences[:i+1]
            # Add that sequence to our array of sequences
            sequences.append(sequence)
    # Return our total sequences and the total number of words in our text
    return sequences, total_words

token_conv, total_words = get_sequences(conversations[:5000])

print(token_conv[:5])
print(conversations[0])

def padded_sequences(sequences):
  # So we extract the max length and use that one. Shorter sequences will just use 0's where they don't have words
    max_sequence_length = max([len(x) for x in sequences])
    # Now we have to reshape our sequences to fit to this new length
    # Thankfully keras has the function pad_sequences that does this
    # We then make it an array by calling np.array(padded_sequences)
    sequences = np.array(pad_sequences(sequences, maxlen=max_sequence_length, padding='pre'))

    # Now we split our sequences into data and labels
    # for the phrase "hello new world"
    # we will have the sequences and labels:
    # hello -> new
    # hello new -> world
    # Where each label is the next word we are trying to predict based on the sequence
    data = sequences[:,:-1]
    # So our data will be all the words up to the last one
    label = sequences[:,-1]
    # Our label will be our last word
    # We don't want to assign greater importance to certain words just because they have a bigger number
    # So we make them all arrays of 0 and 1.
    # Each one of our labels will have a specific value
    # i.e, hello can be [0, 0, 0, ..... ,  1]
    # the length depends on the number of words we can have

    label = ku.to_categorical(label, num_classes=total_words)
    return data, label, max_sequence_length

padded_conv, label_conv, max_sequence_length = padded_sequences(token_conv[:20000])

print(padded_conv[0])

# Declare a sequential model
model = Sequential()
# Add a layer to the model (Embedding) that will allow us to take the inputs
model.add(Embedding(total_words, 10, input_length=max_sequence_length - 1)) # because its not 0-based
# Add an LSTM Layer with 100 units (disregard 20% of the parameters)#
#Too many = overfitting
model.add(LSTM(100))
model.add(Dropout(0.2))
# Add another layer (our output layer) with softmax actiavtion
model.add(Dense(total_words, activation='softmax'))
# Compile model with adam optimizer
model.compile(loss='categorical_crossentropy', optimizer='adam')

model.summary()

model.fit(padded_conv, label_conv, epochs=100, verbose=2)

def generate_text(seed_text, model, max_sequence_len):
    for _ in range(50):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict_classes(token_list, verbose=0)

        output_word = ""
        for word,index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " "+output_word
    return seed_text.title()

print (generate_text("What is the capital of Peru?", model, max_sequence_length))
