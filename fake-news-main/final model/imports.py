import keras
import numpy as np
import tensorflow as tf
import re
import pandas as pd
import webbrowser
#import TokenLSTM
#"just for the first time, then re comment it"
from keras.models import model_from_json
#from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize 
from keras.preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from tensorflow.keras import models,layers
from flask import Flask, render_template , request, url_for
import pickle
import emoji
import itertools
# Importing libraries
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import LSTM
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.convolutional import  AveragePooling1D
from keras.layers.embeddings import Embedding
from sklearn.metrics import  accuracy_score
from keras.preprocessing import sequence
import preprocessing_process
import readDataset
import extra_features
#import Embedding as embedding


from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
#import preprocessing as p
# Import packages
#from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
__all__ = [
    'keras',
    'np',
    'tf',
    're',
    'pd',
    'webbrowser',
    'model_from_json',
    'word_tokenize',
    'pad_sequences',
    'Tokenizer',
    'train_test_split',
    'models',
    'layers',
    'Flask',
    'render_template',
    'request',
    'url_for',
    'pickle',
    'emoji',
    'itertools',
    'imdb',
    'Sequential',
    'Dense',
    'Flatten',
    'LSTM',
    'Conv1D',
    'MaxPooling1D',
    'AveragePooling1D',
    'Embedding',
    'accuracy_score',
    'sequence',
    'preprocessing_process',
    'readDataset',
    'extra_features',
    'svm',
    'train_test_split',
    'metrics',
    #'Doc2Vec',
    #'TaggedDocument',
    'word_tokenize',
    #'embedding'
]