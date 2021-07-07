import re
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

#stemming
def stemSentence(sentence):
     lancaster = LancasterStemmer()
     token_words = word_tokenize(sentence)
     stem_sentence = []
     for word in token_words:
         stem_sentence.append(lancaster.stem(word))
         stem_sentence.append(" ")
    
     return "".join(stem_sentence)

#lowercase
def lowercase(text):
    text=text.lower()
    return text

#Remove noise
def remove_noise(text):
    for k in text.split("\n"):
        text=re.sub("[^a-zA-Z0-9]+", ' ', k) 
    return text

#stop_words
def stop_word(text):
    text_tokens = word_tokenize(text)
    tokens_without_sw=[word for word in text_tokens if not word in stopwords.words()]
    filtered_sentence = (" ").join(tokens_without_sw)
    return filtered_sentence

def text_preprocessing(text):
    lowercasing=lowercase(text)
    StopWordRemoval=stop_word(lowercasing)
    RemovingNoise=remove_noise(StopWordRemoval)
    Stemming=stemSentence(RemovingNoise)
    return Stemming 