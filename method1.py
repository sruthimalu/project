
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


def meth1():

    df=pd.read_csv('processed.csv')
    X=df['request'].values
    y=df['classification'].values.astype('uint')
    oversample = SMOTE()

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3)



    import pickle

    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(X_train)
    f=open('tokenizer.pkl','wb')
    pickle.dump(tokenizer,f)
    f.close()


    X_train = tokenizer.texts_to_sequences(X_train)
    X_test = tokenizer.texts_to_sequences(X_test)

    vocab_size = len(tokenizer.word_index) + 1

    maxlen = 100

    X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
    X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

    X_train, Y_train = oversample.fit_resample(X_train, Y_train.astype('int'))

    from models import model1

    M1=model1(maxlen)
    M1.fit(X_train,Y_train,epochs=20,batch_size=128,validation_data=(X_test,Y_test))
    M1.save('M1.model')
    return M1