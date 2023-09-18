import yfinance as yf

crypto = input("Type crypto symbol: ")
crypto.upper()

msft = yf.Ticker(f"{crypto}-USD")
df = yf.download(
tickers = f"{crypto}-USD",
period = "1mo",
interval = "15m"
)
print(crypto.upper() + "-USD")
print(df)

