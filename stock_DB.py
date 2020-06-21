import FinanceDataReader as fdr

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost',27017)
db = client.dbsparta


# 한국
# 심볼	거래소
# KRX	KRX 종목 전체
# KOSPI	KOSPI 종목
# KOSDAQ	KOSDAQ 종목
# KONEX	KONEX 종목
# 미국
# 심볼	거래소
# NASDAQ	나스닥 종목
# NYSE	뉴욕 증권거래소 종목
# AMEX	AMEX 종목
# SP500	S&P 500 종목
df = fdr.StockListing('NYSE')
symbol = df['Symbol']
name = df['Name']

for i in range(len(df['Symbol'])):
    doc = {
    'Symbol' :symbol[i],
    'Name' :name[i] 
    }   
    db.STOCK.insert_one(doc)
    print(doc)
