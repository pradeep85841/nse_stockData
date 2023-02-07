import pandas as pd
from datetime import date
from fastapi import FastAPI
import yfinance as yf

app = FastAPI()



@app.get("/pastdata")
def pastdata(symbol, start:date, end:date):
    if symbol is None:
        text = "incomplete information provided"
        return text
    else:
       data = yf.download(symbol+".NS", start=start, end=end)
       df = pd.DataFrame({"Open":data.Open[0],"High":data.High[0],"Low":data.Low[0],"Close":data.Close[0]}, index=[0])
       return(df.to_json())



@app.get("/financeratio")
def livedata(symbol):
    if symbol is None:
        text = "incomplete information provided"
        return text
    else:
        stock = symbol+".NS"
        data = yf.Ticker(stock)
        info =  data.info
        return info

