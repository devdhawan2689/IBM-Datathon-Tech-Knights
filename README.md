
This Github Repository Contains the Complete Code submitted by the group Tech Kinghts for IBM Datathon 2024.

The Topic that we had chosen for the theme "Tech For Good" was "Spam Call Detection". 

There are 2 Parts of the Project.
a) The First Part Deals with Converting 'Speech to Text'. 
Since listening to people's conversation is also considered a privacy invasion, we wanted to use a model that could work offline and did not require any data to be sent to a third party or any remote server. 
Therefore we chose 'vosk' for our 'Speech to Text' Model. 

![image](https://github.com/user-attachments/assets/0e348e09-9a1a-4753-bd38-52f1e4138f93)

Vosk is an Open Source speech recognition toolkit. The best things in Vosk are:

1. Supports 20+ languages and dialects - English, Indian English, German, French, Spanish, Portuguese, Chinese, Russian, Turkish, Vietnamese, Italian, Dutch, Catalan, Arabic, Greek, Farsi, Filipino, Ukrainian, Kazakh, Swedish, Japanese, Esperanto, Hindi, Czech, Polish, Uzbek, Korean, Breton, Gujarati, Tajik. More to come.
2. Works offline, even on lightweight devices - Raspberry Pi, Android, iOS
3. Installs with simple pip3 install vosk
4. Portable per-language models are only 50Mb each, but there are much bigger server models available.
5. Provides streaming API for the best user experience (unlike popular speech-recognition python packages)
6. There are bindings for different programming languages, too - java/csharp/javascript etc.
7. Allows quick reconfiguration of vocabulary for best accuracy.
8. Supports speaker identification beside simple speech recognition. 

b) The Second Part of the project deals with NLP. 
Once we have our Speech to Text data from vosk, we then need to have a Model inplace to check if the Call is Scam or not.
We trained our Spam Call Dataset Containing around 107970 rows of sentences that are classified as fraud or normal. 
Using  NLTK and Scikit Learn, we trained our Dataset on MultinomialNB() Model, which had shown to provide the highest accuracy. 

![image](https://github.com/user-attachments/assets/0756c275-0e0c-4d4d-9ba8-814f7757436d)

**The 'Final_Model.ipynb' contains the entire code for NLP part of the project and was built using IBM's LinuxOne Machine.** 

The 'Combined_Code.py' contains the final code of the project. 

Demo Of The Project can be seen here - https://youtu.be/UM-4urqgJDU 
 
Spam Call 
![2022-09-16 01-20-55 00_00_38_55 Still023](https://github.com/user-attachments/assets/4ef41f68-31d0-46bc-8a64-4b39b55fecf4)

Normal Call
![2022-09-16 01-20-55 00_01_14_08 Still024](https://github.com/user-attachments/assets/a8e412f6-b2e4-483f-83d9-2be7fd5c0ea1)
