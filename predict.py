from keras.models import load_model
import pickle
import pandas as pd 
import re
import nltk
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import np_utils
from imblearn.over_sampling import SMOTE
from collections import Counter
from sklearn.ensemble import Ensemble

model1=load_model('M1.model')
model2=load_model('M2.model')
model3=load_model('M3.model')


tokenizer=pickle.load(open('tokenizer.pkl','rb'))

def predict1(url):
    e=Ensemble('','','')
    
    url=[url]
    url=tokenizer.texts_to_sequences(url)
    max_len=100
    url=pad_sequences(url,padding='post',maxlen=max_len)
    print(url)
    pred=e.predict(model1,model2,model3,url)[0][0]
    print(pred)
    if pred>0.5:
        return 1
    else:
        return 0    

if __name__=="__main__":
    url1='/tienda1/publico/anadir.jsp /id=3&nombre=Vino+Rioja&precio=100&cantidad=55&B1=A%F1adir+al+carrito'
    url2='/tienda1/publico/entrar.jsp /errorMsg=Credenciales+incorrectas%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E'
    predict1(url2)

