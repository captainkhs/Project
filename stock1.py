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

client = MongoClient('localhost', 27017)
db = client.dbsparta

d = date.today() - timedelta(15)
Date = d.isoformat()
 # 1. 클라이언트가 전달한 'name', 'code' 를 name, code 변수에 넣습니다.
name = 'Jack Henry & Associates, Inc.'
symbol = db.STOCK.find_one({'Name': name}, {'_id':False})
symbol = symbol['Symbol']

df = fdr.DataReader(symbol, Date)
# df = df
# df = df.tolist()
print(df.index.strftime('%Y-%m-%d').values)

