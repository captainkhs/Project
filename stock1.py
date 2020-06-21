from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
import FinanceDataReader as fdr
import datetime, time

import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
from collections import OrderedDict
from datetime import datetime
import requests

import FinanceDataReader as fdr
from datetime import date, timedelta

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

d = date.today() - timedelta(15)
Date = d.isoformat()


name = ''
symbol = 'MMM'

symbol = name or symbol

df = fdr.DataReader(symbol, Date)
df = df['Close'].tolist()
print(df)

