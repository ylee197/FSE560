import yfinance as yf
import pandas as pd
import datetime as dt
from datetime import date, timedelta

def load_data(ticker, START, TODAY):
    data = yf.download(ticker, START, TODAY)
    data.dropna(inplace=True)
    data.columns = data.columns.droplevel(1)
    data.reset_index(inplace=True)
    return data

def fetch_stock_data(ticker):
    ## Finding days 
    today = date.today()
    month_ago = today - timedelta(days=60)
    roll_out_days = 5
    while(month_ago.strftime("%A")!='Monday'):
        month_ago += timedelta(days=1)
    TODAY = today.strftime('%Y-%m-%d')
    MonthAgo = month_ago.strftime('%Y-%m-%d')

    ## Download A Month data 
    data = load_data(ticker, MonthAgo, TODAY)
    
    ## Creating Monday to Friday data
    data['Day'] = data['Date'].dt.strftime("%A")
    df = pd.DataFrame()
    i = 0
    while i < (len(data)-5):
            df_days = data.iloc[[i]].copy()
            i += 1
            while data.loc[i,'Day'] != 'Monday':
                    df_days = pd.concat([df_days,data.iloc[[i]]], ignore_index=True)
                    i += 1
            if(len(df_days) == 5):
                    df = pd.concat([df, df_days], ignore_index=True)
    df = pd.concat([df, data[i:len(data)]], ignore_index=True)
    df = df.tail(30)
    df = df.reset_index(drop=True)
    return df