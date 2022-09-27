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
import re
from bs4 import BeautifulSoup
import string 




f=open('js.txt','r')
js=f.readlines()
js=[i.replace('\n','') for i in js]
f.close()
#print(js)


f=open('sql.txt','r')
sql=f.readlines()
sql=[i.replace('\n','') for i in sql]
f.close()
#print(sql)

def spaced(x):
    return ' '+x+' '



def transform(x):
    # print(x)
    res = re.sub(r'[^\w\s<>]', ' ',x)
    # print(res)
    html=[]
    res1=res.split()
    # print(res1)
    for i in res1:
        if bool(BeautifulSoup(i, "html.parser").find()):
            st1=0
            st2=-1
            s=i[i.find('<'):i.find('>')+1]
            html.append(i)
    # print(html)
    s=''

    for i in res1:
        if i.upper() in sql:
            continue 
        if i in js:
            continue    
        if i in html:
            s=i[i.find('<'):i.find('>')+1]

        i=i.replace(s,'')  
        if i.isalpha():
            x=x.replace(i,'purestring') 
        else:
            x=x.replace(i,'mixedstring')

    # print(x) 
    for i in string.punctuation:
        x=x.replace(i,spaced(i))
    return x

def meth2():

    df=pd.read_csv('processed.csv')
    df['request']=df['request'].apply(transform)
    X=df['request'].values
    y=df['classification'].values.astype('uint')

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3)

    import pickle

    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(X_train)
    f=open('tokenizer1.pkl','wb')
    pickle.dump(tokenizer,f)
    f.close()


    X_train = tokenizer.texts_to_sequences(X_train)
    X_test = tokenizer.texts_to_sequences(X_test)

    vocab_size = len(tokenizer.word_index) + 1

    maxlen = 100

    X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
    X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)



    from models import MRN

    M1=MRN(maxlen)
    M1.fit(X_train,Y_train,epochs=20,batch_size=128,validation_data=(X_test,Y_test))
    M1.save('M2.model')

if __name__=="__main__":
    # str1=X[0]
    # str1=str1+'<script>'
    # t=transform(str1)
    # print(t)
    pass