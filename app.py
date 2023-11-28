import yfinance as yf
import streamlit as st
# Titles and subtitles
st.title("Crypto Trading Bot")

# Defining ticker variables
Bitcoin ='BTC-USD'
Ethereum = 'ETH-USD'
Litecoin = 'LTC-USD'

# Accessing data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
LTC_Data = yf.Ticker(Litecoin)

# Fetch history data from Yahoo Finance
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
LTCHis = LTC_Data.history(period="max")

BTC = yf.download(Bitcoin, start="2023-11-01", end="2023-11-28")
ETH = yf.download(Ethereum, start="2023-11-01", end="2023-11-28")
LTC = yf.download(Litecoin, start="2023-11-01", end="2023-11-28")

# Function to format the date column without time
def format_date_column(data):
    data.reset_index(inplace=True)
    data['Date'] = data['Date'].dt.date  # Extracting only the date component
    data.set_index('Date', inplace=True)
    return data

# Formatting date columns for each cryptocurrency
BTC = format_date_column(BTC)
ETH = format_date_column(ETH)
LTC = format_date_column(LTC)
# Function to determine Buy or Sell based on the trend
def determine_action(data):
    if data['Close'].iloc[-1] > data['Close'].iloc[0]:
        return "Sell"
    elif data['Close'].iloc[-1] < data['Close'].iloc[0]:
        return "Buy"
    else:
        return "Hold"

# Bitcoin
st.write("Bitcoin ($)")
# Display dataframe
st.table(BTC)
# Display a chart
st.bar_chart(BTCHis.Close)
# Determine and display Buy/Sell action for Bitcoin
btc_action = determine_action(BTC)
st.write(f"Prediction: {btc_action}")

# Ethereum
st.write("Ethereum ($)")
# Display dataframe
st.table(ETH)
# Display a chart
st.bar_chart(ETHHis.Close)
# Determine and display Buy/Sell action for Ethereum
eth_action = determine_action(ETH)
st.write(f"Prediction: {eth_action}")

# Litecoin
st.write("Litecoin ($)")
# Display dataframe
st.table(LTC)
# Display a chart
st.bar_chart(LTCHis.Close)
# Determine and display Buy/Sell action for Litecoin
ltc_action = determine_action(LTC)
st.write(f"Prediction: {ltc_action}")
