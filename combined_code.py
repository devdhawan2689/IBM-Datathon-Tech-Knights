import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import preprocessing

import numpy as np
import pickle

import string
import nltk
from nltk.corpus import stopwords

from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer

from sklearn.model_selection import train_test_split 
from sklearn import metrics

from sklearn.feature_extraction.text import TfidfVectorizer

# Imports for Speech To Text
import vosk
import pyaudio
import json


# Running Model
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

with open('tfidf_vectorizer.pkl', 'rb') as file:
    bow_transformer = pickle.load(file)

with open('messages_bow.pkl', 'rb') as file:
    messages_bow = pickle.load(file)

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer().fit(messages_bow)

def runPrediction(text):
    test = bow_transformer.transform([text])
    # print(test)
    # print(test.shape)
    test = tfidf_transformer.transform(test)

    return loaded_model.predict(test)[0] 

high_risk_words = pd.read_csv('high_risk_words.csv')
high_risk_words = list(high_risk_words['words'])

# runPrediction("Dear we have need your Number for confirmation")


## Running Speech To Text

# Here I have downloaded this model to my PC, extracted the files 
# and saved it in local directory
# Set the model path
model_path = "C:/Users/admin/.cache/vosk/vosk-model-en-us-0.22/"
# Initialize the model with model-path
model = vosk.Model(model_path)



#if you don't want to download the model, just mention "lang" argument 
#in vosk.Model() and it will download the right  model, here the language is 
#US-English
#model = vosk.Model(lang="en-us")

# Create a recognizer
rec = vosk.KaldiRecognizer(model, 16000)

# Open the microphone stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8192)

# Specify the path for the output text file
output_file_path = "recognized_text.txt"

threat_threshold = 0

# Open a text file in write mode using a 'with' block
with open(output_file_path, "w") as output_file:
    print("Listening To The Call for Any Potential Threat!\n\n")
    # Start streaming and recognize speech
    while True:
        data = stream.read(8192)#read in chunks of 4096 bytes
        if rec.AcceptWaveform(data):#accept waveform of input voice
            # Parse the JSON result and get the recognized text
            result = json.loads(rec.Result())
            recognized_text = result['text']
            
            # Write recognized text to the file
            output_file.write(recognized_text + "\n")
            print(recognized_text)
            
            if runPrediction(recognized_text) == 1:
                checkFlag = False

                for word in high_risk_words:
                    if word in recognized_text:
                        threat_threshold = threat_threshold + 30
                        checkFlag = True
                
                if checkFlag == False:
                    threat_threshold = threat_threshold + 10
                

            print(f"\nThreat Likely {threat_threshold}%\n")

            if threat_threshold >= 80:
                print("\nHIGH RISK OF THREAT DETECTED, DISCONNECTING THE CALL!")
                break

            # Check for the termination keyword
            if "bye bye" in recognized_text.lower():
                print("CALL ENDED BY THE USER!")
                break


# Stop and close the stream
stream.stop_stream()
stream.close()

# Terminate the PyAudio object
p.terminate() 


