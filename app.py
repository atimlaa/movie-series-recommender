from flask import Flask
import numpy as np
import pandas as pd
app = Flask(__name__)


amazon_prime = pd.read_csv('data/amazon-prime-data.csv')
apple_tv = pd.read_csv('data/apple-tv-data.csv')
disney_plus = pd.read_csv('data/disney-plus-data.csv')
hbo_max = pd.read_csv('data/hbo-max-data.csv')
netflix = pd.read_csv('data/netflix-data.csv')
paramount = pd.read_csv('data/paramount-data.csv')

@app.route("/")
def home():
    return "Hello, Flask!"