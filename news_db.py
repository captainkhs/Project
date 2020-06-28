import requests
from bs4 import BeautifulSoup
import bs4.element
import datetime

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost',27017)
db = client.dbsparta

# '경제', '사회', '생활/문화', '세계', 'IT/과학'
# 각 분야의 상위 3개 뉴스들을 가져옵니다. (5분야 * 3개 = 15개)
def get_naver_news_top3():
    db.NEWS.drop()
    
    # 뉴스를 가져올 링크 주소 지정
    base_url = "https://news.naver.com"
    today = datetime.datetime.today().strftime('%Y%m%d')
    news_params = "/main/ranking/popularDay.nhn?rankingType=popular_day&date=" + today + "&sectionId="
        
    
    # 뉴스 결과를 담아낼 dictionary
    news_dic = dict()
    
    # sections : '경제', '사회', '생활/문화', '세계', 'IT/과학'
    # section_ids :  URL에 사용될 뉴스  각 부문 ID
    # sections = ["eco","soc","lif","wor","its"]
    # section_ids = ["101","102","103","104","105"]
    sections = ["eco"]
    section_ids = ["101"]
    for sec, sid in zip(sections, section_ids):
        # 해당 분야 상위 뉴스 목록 주소
        news_link = base_url + news_params + sid
        
        
        # 해당 분야 상위 뉴스 HTML 가져오기
        res = requests.get(news_link)
        soup = BeautifulSoup(res.text,'lxml')
        
        # 해당 분야 상위 뉴스 3개 가져오기
        lis3 = soup.find_all('li', class_='ranking_item', limit=10)
        
        
        # 가져온 뉴스 데이터 정제하기
        news_list3 = []
        default_img = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=naver#"
        for li in lis3:
            news_link = base_url + li.a.attrs.get('href')
            
            res = requests.get(news_link)
            soup = BeautifulSoup(res.text,'lxml')
            body = soup.find('div', class_="_article_body_contents")
            
            # 뉴스 본문 가져오기
            news_body = ''
            for content in body:
                if type(content) is bs4.element.NavigableString and len(content) > 50:
                    # content.strip() : whitepace 제거 (참고 : https://www.tutorialspoint.com/python3/string_strip.htm)
                    news_body += content.strip() + ' '
                    # news_body += content.strip()
                    # 뉴스 요약할 때, '.' 마침표 뒤에 한칸 띄워주지 않으면 문장을 구분 못하는 경우가 있음
                        
            # title : 뉴스 제목
            # views : 조회수
            # link : 뉴스 URL
            # news_body : 뉴스 내용
            # image_url : 이미지 URL
            news_info = {
                "title" : li.a.attrs.get('title'),
                "views" : li.find('div', class_="ranking_view").text,
                "link" : news_link,
                "news_body" : news_body[0:50],
                "image_url" : li.img.attrs.get('src') if li.img else default_img
            }
            
            news_list3.append(news_info)
            
            db.NEWS.insert_one(news_info)
        news_dic[sec] = news_list3
        

    return news_dic



    