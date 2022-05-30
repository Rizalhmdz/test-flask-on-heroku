#app/main.py

# from cProfile import label
# import re
from flask import Flask
# import tensorflow as tf
# import numpy as np
import pandas as pd
# from sklearn.model_selection import train_test_split

app = Flask(__name__)

from flask import Flask

# app = Flask(__name__)
# model = pickle.load(open('verifIDNews_model.pkl','rb'))

@app.route('/')
def home():
    return 'end point data sms : \"/api/sms/\"'

@app.route('/api/sms',methods=['GET'])
def predict():
    
    # user_input = [request.form.get('input')]
    path = 'dataset_sms_spam_v1.csv'

    dataframe = pd.read_csv( path , encoding='iso8859')
    json = dataframe.to_json(orient='records')
    
    # data_json = list()

    # for a, i in dataframe['Teks'], dataframe['label'] :
    #             data_json.append({"texr": a, "label": i})
                
    return json
    
    # max_features = 10000
    # maxlen = 300
    # return 
# jsonify(
#             data_json
#         )
    
#     tokenizer = text.Tokenizer(num_words = max_features)
#     tokenized_test = tokenizer.texts_to_sequences(user_input)
#     user_input_tokenized = sequence.pad_sequences(tokenized_test, maxlen = maxlen)
#     output = model.predict(user_input_tokenized)
    
#     label = ''
    
#     if output > 0.75 : 
#         label = 'Berita Terindikasi sebagai Fakta'
#     elif output <= 0.75 and output > 0.60 : 
#         label = 'Berita Terindikasi lemah Fakta'
#     elif output <= 0.6 and output > 0.5 :
#         label = 'Berita perlu ditinjau ulang antara Fakta atau Hoax'
#     elif output <= 0.5 and output > 0.35 : 
#         label = 'Berita Terindikasi Lemah sebagai Hoax'
#     elif output <= 0.35 and output > 0.15 : 
#         label = 'Berita Terindikasi sebagai Hoax'
#     elif output <= 0.15 :
#         label = 'Berita Terindikasi Kuat sebagai Hoax'

