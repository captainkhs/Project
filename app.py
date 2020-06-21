
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

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/currency', methods=['GET'])
def read_currency():
   r = requests.get('https://earthquake.kr:23490/query/USDKRW,CNYKRW,EURKRW,JPYKRW')
   return  r.json()

@app.route('/korindices', methods=['GET'])
def read_korindices():
   URL = "https://kr.investing.com/indices/south-korea-indices"
   req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
   res = urllib.request.urlopen(req)
   source = res.read()
   res.close()
   soup = BeautifulSoup(source, 'html.parser')
   #KOSPI--------------------------------------------------
   kospi = soup.findAll("td",class_="pid-37426-last")
   KOSPI = kospi[0].text                                                  #코스피 지수
   kospi_inde = soup.findAll("td",class_="pid-37426-pc")
   KOSPI_INDE = kospi_inde[0].text                                        #지수 변동폭
   kospi_width = soup.findAll("td",class_="pid-37426-pcp")
   KOSPI_WIDTH = kospi_width[0].text                                      #지수 등락률
   #KOSDAQ-------------------------------------------------
   kosdaq = soup.findAll("td",class_="pid-38016-last")
   KOSDAQ = kosdaq[0].text                                                #코스닥 지수
   kosdaq_inde = soup.findAll("td",class_="pid-38016-pc")
   KOSDAQ_INDE = kosdaq_inde[0].text                                      #지수 변동폭
   kosdaq_width = soup.findAll("td",class_="pid-38016-pcp")
   KOSDAQ_WIDTH = kosdaq_width[0].text                                    #지수 등락률
   stock = {
               'KOSPI' : KOSPI,
               'KOSPI_INDE' : KOSPI_INDE,
               'KOSPI_WIDTH' : KOSPI_WIDTH,
               'KOSDAQ' : KOSDAQ,
               'KOSDAQ_INDE' : KOSDAQ_INDE,
               'KOSDAQ_WIDTH' : KOSDAQ_WIDTH,
         }
   return  stock

@app.route('/amrindices', methods=['GET'])
def read_amrindices():
   URL = "https://kr.investing.com/indices/usa-indices"
   req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
   res = urllib.request.urlopen(req)
   source = res.read()
   res.close()
   soup = BeautifulSoup(source, 'html.parser')
   #S&P500-------------------------------------------------
   snp = soup.findAll("td",class_="pid-166-last")
   SNP = snp[0].text                                                #SNP 지수
   snp_inde = soup.findAll("td",class_="pid-166-pc")
   SNP_INDE = snp_inde[0].text                                      #지수 변동폭
   snp_width = soup.findAll("td",class_="pid-166-pcp")
   SNP_WIDTH = snp_width[0].text                                    #지수 등락률
   #NASDAQ-------------------------------------------------
   nasdaq = soup.findAll("td",class_="pid-14958-last")
   NASDAQ = nasdaq[0].text                                                #NASDAQ 지수
   nasdaq_inde = soup.findAll("td",class_="pid-14958-pc")
   NASDAQ_INDE = nasdaq_inde[0].text                                      #지수 변동폭
   nasdaq_width = soup.findAll("td",class_="pid-14958-pcp")
   NASDAQ_WIDTH = nasdaq_width[0].text                                    #지수 등락률
   #DOW-------------------------------------------------
   dji = soup.findAll("td",class_="pid-169-last")
   DJI = dji[0].text                                                #DOW 지수
   dji_inde = soup.findAll("td",class_="pid-169-pc")
   DJI_INDE = dji_inde[0].text                                      #지수 변동폭
   dji_width = soup.findAll("td",class_="pid-169-pcp")
   DJI_WIDTH = dji_width[0].text                                    #지수 등락률
   stock = {
               'SNP' : SNP,
               'SNP_INDE' : SNP_INDE,
               'SNP_WIDTH' : SNP_WIDTH,
               'NASDAQ' : NASDAQ,
               'NASDAQ_INDE' : NASDAQ_INDE,
               'NASDAQ_WIDTH' : NASDAQ_WIDTH,
               'DJI' : DJI,
               'DJI_INDE' : DJI_INDE,
               'DJI_WIDTH' : DJI_WIDTH,
         }
   return  stock

@app.route('/api/search', methods=['POST'])
def stock_search():
   d = date.today() - timedelta(15)
   Date = d.isoformat()
 # 1. 클라이언트가 전달한 'name', 'code' 를 name, code 변수에 넣습니다.
   name = request.form['name'] 
   symbol = db.STOCK.find_one({'Name': name}, {'_id':False})
   symbol = symbol['Symbol']

   df = fdr.DataReader(symbol, Date)
   df = df['Close']
   df = df.tolist()

   return  jsonify({'result': 'success','df_list': df, 'symbol':symbol, 'name':name})




    


if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)





