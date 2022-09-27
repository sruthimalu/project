from keras.layers import Input, Dense, Embedding, Conv1D, MaxPooling1D,LSTM,GRU,GlobalAveragePooling1D,ReLU
from keras.layers import Reshape, Flatten, Dropout, Concatenate,Bidirectional,concatenate,BatchNormalization,add
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam
from keras.models import Model,Sequential
from sklearn.model_selection import train_test_split

def model1(n):
    embedding_vecor_length = 32
    max_len=n
    model = Sequential()
    model.add(Embedding(5000, embedding_vecor_length, input_length=max_len))
    model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(LSTM(50))
    model.add(Dense(10))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def MRN(n):
    input1=Input(shape=(n,))
    embedding_vecor_length = 32
    
    emb1=Embedding(5000, embedding_vecor_length)(input1)

    '''block_1'''
    b1_cnv2d_1 = Conv1D(filters=16, kernel_size=1, padding='same',
                    use_bias=False, name='b1_cnv2d_1', kernel_initializer='normal')(emb1)
    b1_relu_1 = ReLU(name='b1_relu_1')(b1_cnv2d_1)
    b1_bn_1 = BatchNormalization(epsilon=1e-3, momentum=0.999, name='b1_bn_1')(b1_relu_1)  # size: 14*14

    b1_cnv2d_2 = Conv1D(filters=32, kernel_size=1, padding='same',
                        use_bias=False, name='b1_cnv2d_2', kernel_initializer='normal')(b1_bn_1)
    b1_relu_2 = ReLU(name='b1_relu_2')(b1_cnv2d_2)
    b1_out = BatchNormalization(epsilon=1e-3, momentum=0.999, name='b1_out')(b1_relu_2)  # size: 14*14

    '''block 2'''
    b2_cnv2d_1 = Conv1D(filters=32, kernel_size=1, padding='same',
                        use_bias=False, name='b2_cnv2d_1', kernel_initializer='normal')(b1_out)
    b2_relu_1 = ReLU(name='b2_relu_1')(b2_cnv2d_1)
    b2_bn_1 = BatchNormalization(epsilon=1e-3, momentum=0.999, name='b2_bn_1')(b2_relu_1)  # size: 14*14

    b2_add = add([b1_out, b2_bn_1])  #

    b2_cnv2d_2 = Conv1D(filters=64, kernel_size=3,padding='same',
                        use_bias=False, name='b2_cnv2d_2', kernel_initializer='normal')(b2_add)
    b2_relu_2 = ReLU(name='b2_relu_2')(b2_cnv2d_2)
    b2_out = BatchNormalization(epsilon=1e-3, momentum=0.999, name='b2_bn_2')(b2_relu_2)  # size: 7*7

    '''block 3'''
    b3_cnv2d_1 = Conv1D(filters=64, kernel_size=1, padding='same',
                        use_bias=False, name='b3_cnv2d_1', kernel_initializer='normal')(b2_out)
    b3_relu_1 = ReLU(name='b3_relu_1')(b3_cnv2d_1)
    b3_bn_1 = BatchNormalization(epsilon=1e-3, momentum=0.999, name='b3_bn_1')(b3_relu_1)  # size: 7*7

    b3_add = add([b2_out, b3_bn_1])  #

    b3_cnv2d_2 = Conv1D(filters=128, kernel_size=3, padding='same',
                        use_bias=False, name='b3_cnv2d_2', kernel_initializer='normal')(b3_add)
    b3_relu_2 = ReLU(name='b3_relu_2')(b3_cnv2d_2)
    b3_out = BatchNormalization(epsilon=1e-3, momentum=0.999, name='b3_out')(b3_relu_2)  # size: 3*3

    '''block 4'''
    b4_avg_p = GlobalAveragePooling1D()(b3_out)
    output = Dense(1, name='model_output', activation='sigmoid',
                kernel_initializer='he_uniform')(b4_avg_p)

    model = Model(input1, output)

    model_json = model.to_json()

    with open("mrn.json", "w") as json_file:
        json_file.write(model_json)
    model.summary()
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model    



def model_cnn(n):
    embedding_vecor_length = 32
    max_len=n
    model = Sequential()
    model.add(Embedding(5000, embedding_vecor_length, input_length=max_len))
    model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(filters=64, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(filters=128, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(100))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model



if __name__=="__main__":
    MRN(100)