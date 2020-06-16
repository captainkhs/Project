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

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'nanummyeongjo'
plt.rcParams["figure.figsize"] = (14,4)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams["axes.grid"] = True


# URL = "https://kr.investing.com/indices/south-korea-indices"
# req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
# res = urllib.request.urlopen(req)
# source = res.read()
# res.close()
# soup = BeautifulSoup(source, 'html.parser')
# #KOSPI--------------------------------------------------
# kospi = soup.findAll("td",class_="pid-37426-last")
# KOSPI = kospi[0].text
# kospi_inde = soup.findAll("td",class_="pid-37426-pc")
# KOSPI_INDE = kospi_inde[0].text
# kospi_inde_wid = soup.findAll("td",class_="pid-37426-pcp")
# KOSPI_INDE_WID = kospi_inde_wid[0].text

# #KOSDAQ-------------------------------------------------
# kosdaq = soup.findAll("td",class_="pid-37426-last")
# KOSDAQ = kosdaq[0].text
# kosdaq_inde = soup.findAll("td",class_="pid-38016-pc")
# KOSDAQ_INDE = kosdaq_inde[0].text
# kosdaq_inde_wid = soup.findAll("td",class_="pid-38016-pcp")
# KOSDAQ_INDE_WID = kosdaq_inde_wid[0].text

# stock = {
#             'KOSPI' : KOSPI,
#             'kKOSPI_INDE' : KOSPI_INDE,
#             'kKOSPI_INDE_WID' : KOSPI_INDE_WID,
#             'kKOSDAQ' : KOSDAQ,
#             'kKOSDAQ_INDE' : KOSDAQ_INDE,
#             'kKOSDAQ_INDE_WID' : KOSDAQ_INDE_WID,
#         }

# URL = "https://kr.investing.com/indices/usa-indices"
# req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
# res = urllib.request.urlopen(req)
# source = res.read()
# res.close()
# soup = BeautifulSoup(source, 'html.parser')
# #S&P500-------------------------------------------------
# snp = soup.findAll("td",class_="pid-166-last")
# SNP = snp[0].text                                                #SNP 지수
# snp_inde = soup.findAll("td",class_="pid-166-pc")
# SNP_INDE = snp_inde[0].text                                      #지수 변동폭
# snp_width = soup.findAll("td",class_="pid-166-pcp")
# SNP_WIDTH = snp_width[0].text                                    #지수 등락률
# stock = {
#                'SNP' : SNP,
#                'SNP_INDE' : SNP_INDE,
#                'SNP_WIDTH' : SNP_WIDTH,

#          }
# print(stock) 

df = fdr.DataReader('KS11', '2010')
ks11_df = list(df['Close'])

print(ks11_df)