import FinanceDataReader as fdr
import datetime, time

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


d = datetime.date.today()
date = d.isoformat()
# #----------------------------------
# # usdkrw = fdr.DataReader('USD/KRW', date)
# # usdkrw = usdkrw['Close']
# # usdkrw = usdkrw.to_list()
# #-----------------------------------

# # DJI	다우존스 지수
# # IXIC	나스닥 지수
# # US500	S&P 500 지수
# # VIX	S&P 500 VIX
# # KS11	KOSPI 지수
# # KQ11	KOSDAQ 지수

# dji = fdr.DataReader('DJI', date)         #휴일의 경우 키에러가 발생함.
# dji_1 = dji['Close']
# dji_1= dji_1[0]
# dji_5 = dji['Change']
# dji_5 = dji_5[0]
# doc = {
#         'date': date,
#         'value': dji_1,
#         'change': dji_5 ,
#       }
# db.nasdaq.insert_one(doc)

# ixic = fdr.DataReader('IXIC', date)         #휴일의 경우 키에러가 발생함.
# ixic_1 = ixic['Close']
# ixic_1= ixic_1[0]
# ixic_5 = ixic['Change']
# ixic_5 = ixic_5[0]
# doc = {
#         'date': date,
#         'value': ixic_1,
#         'change': ixic_5 ,
#       }
# db.nasdaq.insert_one(doc)

# us500 = fdr.DataReader('US500', date)         #휴일의 경우 키에러가 발생함.
# us500_1 = us500['Close']
# us500_1= us500_1[0]
# us500_5 = us500['Change']
# us500_5 = us500_5[0]
# doc = {
#         'date': date,
#         'value': us500_1,
#         'change': us500_5 ,
#       }
# db.us500.insert_one(doc)

# ks11 = fdr.DataReader('KS11', date)         #휴일의 경우 키에러가 발생함.
# ks11_1 = ks11['Close']
# ks11_1= ks11_1[0]
# ks11_5 = ks11['Change']
# ks11_5 = ks11_5[0]
# doc = {
#         'date': date,
#         'value': ks11_1,
#         'change': ks11_5 ,
#       }
# db.kospi.insert_one(doc)


# kq11 = fdr.DataReader('KQ11', date)         #휴일의 경우 키에러가 발생함.
# kq11_1 = kq11['Close']
# kq11_1= kq11_1[0]
# kq11_5 = kq11['Change']
# kq11_5 = kq11_5[0]
# doc = {
#         'date': date,
#         'value': kq11_1,
#         'change': kq11_5 ,
#       }
# db.kosdaq.insert_one(doc)

# nasdaq = list(db.nasdaq.find())
# nasdaq = nasdaq[1]['value']
# us500 = list(db.us500.find())
# us500 = us500[1]['value']

# kq11 = list(db.kosdaq.find())
# value = kq11[0]['value']
# change = kq11[0]['change']
# print(value, change)


df = fdr.DataReader('KS11', date)
ks11_df = df['Close']

doc ={
    'date' : date,
    'data' : ks11_df
    }

print(doc)