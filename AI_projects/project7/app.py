import streamlit as st
import pandas as pd
import keras
import datetime as dt
from datetime import date, timedelta
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import tensorflow as tf
from fine_tuning import LSTM_Model 

from stock_data import fetch_stock_data

st.title("Stock Price Direction and Change Prediction")

ticker = st.text_input("Enter stock ticker symbol")
roll_out_days = 5
print("Ticker:",ticker)

if ticker:
    df = fetch_stock_data(ticker)
    st.write("One Month Data", df.tail())
    y_pred = LSTM_Model(df, roll_out_days)
    df_result = df[['Date','Close']]

    df_final = df_result[6:]
    df_final = df_final.reset_index(drop = True)
    max_day = df_final['Date'].max().strftime('%Y-%m-%d')
    more_day = (df_final['Date'].max()+timedelta(days=roll_out_days)).strftime('%Y-%m-%d')
   
    dates = pd.date_range(start=max_day, end=more_day, freq='D')
    df_extra = pd.DataFrame({'Date': dates, 'Close':np.nan, 'Pred':np.nan})
    df_final = pd.concat([df_final,df_extra], ignore_index=True)
    df_final['Pred'] = y_pred
 
    st.markdown("**Predicting for Next 5 Days Stock Price:**")
    st.dataframe(df_final.tail(5))

    # Ploting a graph
    st.markdown("**Ploting a Graph from 30 Days ago and 5 Days Stock Price Prediction.**")
    plt.figure(figsize = (12,6))
    plt.plot('Date','Close',data = df_final, color='b', label = 'Original Price')
    plt.plot('Date','Pred',data = df_final[:25], color='r', label = 'Predited Price')
    plt.plot('Date','Pred',data = df_final[24:], linestyle='--', color='r', label = 'Predited Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.xticks(rotation=45, ha='right')
    plt.legend(loc='best')
    plt.grid(True)
    #plt.show()
    st.pyplot(plt)
        

        