from stocks import yf_stocks

st =yf_stocks()
st.download_exchange_data(nasdaq).to_csv("Nasdaq_stocks.csv",index=False)
