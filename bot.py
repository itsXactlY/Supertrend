import ccxt

exchange = ccxt.binance()

markets = exchange.load_markets()

for market in markets:
    if 'BNB' in market:
        print(market)

# ticker = exchange.fetch_ticker('ETH/USDT')

# print(ticker)

# ohlc = exchange.fetch_ohlcv('BTC/USDT')

# # print(ohlc)

# for candle in ohlc:
#     print(candle)