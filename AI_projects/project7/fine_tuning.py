import keras
import pandas as pd
import datetime as dt
from datetime import date, timedelta
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

def LSTM_Model(df, roll_out_days):
    scaler = MinMaxScaler(feature_range=(0,1))
    df_close = df[['Close']].values

    norm_array = scaler.fit_transform(df_close)
    train = norm_array[:20]
    test = norm_array[20:]

    trainX = []
    trainY = []
    for i in range(roll_out_days, len(train)):
        trainX.append(train[i-roll_out_days: i])
        trainY.append(train[i,0])
    trainX, trainY = np.array(trainX), np.array(trainY)

    base_model = keras.models.load_model('model.keras')

    #1.Freeze all layers and fine-tune with a tiny learning rate
    for layer in base_model.layers[:-1]:
        layer.trainable = False
    
    #2.Recomplie and train the top layer on new data
    base_model.compile(optimizer = 'adam', loss='mean_absolute_error',metrics=[tf.keras.metrics.MeanAbsoluteError()])
    base_model.fit(trainX, trainY, epochs=30, validation_split =0.2)

    #3.Unfreeze all layers and fine-tune with a tiny learning rate
    for layer in base_model.layers:
        layer.trainable = True

    #4.Recomplie and train the top layer on new data
    base_model.compile(optimizer = 'adam', loss='mean_absolute_error',metrics=[tf.keras.metrics.MeanAbsoluteError()])
    base_model.fit(trainX, trainY, epochs=30, validation_split=0.2)

    testX = []
    testY = []
    for i in range(roll_out_days, len(test)):
        testX.append(test[i-roll_out_days:i])
        testY.append(test[i,0])
    testX, testY = np.array(testX), np.array(testY)

    # Prediction
    y_pred = base_model.predict(testX)

    # Total predict
    total_testX = []
    total_testY = []
    for i in range(roll_out_days, len(norm_array)):
        total_testX.append(norm_array[i-roll_out_days:i])
        total_testY.append(norm_array[i,0])
    total_testX, total_testY = np.array(total_testX), np.array(total_testY)

    total_pred = base_model.predict(total_testX)

    #future 5days value
    new_pred = y_pred[-1]
    new_arr = testX[-1]
    l_pred = []
    for i in range(0, roll_out_days):
        new_pred = new_pred.item()
        new_arr = new_arr[1:roll_out_days]
        new_arr = np.append(new_arr,new_pred)
        new_arr = new_arr.reshape(1,5,1)
        new_pred = base_model.predict(new_arr)
        new_arr = new_arr.reshape(5,1)
        l_pred.append([new_pred[-1].item()])
    
    new_y_pred = np.concatenate((total_pred, l_pred))

    final = scaler.inverse_transform(new_y_pred)
    return final