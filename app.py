from flask import Flask, render_template
import requests
import time
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    return """
    <h1>유병재 못생겼다!</h1>
    <img src = "http://newsimg.hankookilbo.com/2015/06/04/201506041864618664_1.jpg">
    <h3>Hello 병재!!!!!</h3>
    """
    
@app.route('/naver_toon')
def naver_toon():
    #네이버 웹툰을 가져오는 URL 파악
    today = time.strftime("%a").lower()
    naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='+today
    url_base = 'https://comic.naver.com'
    
    #해당 주소로 요청을 보내 정보를 가져온다
    response = requests.get(naver_url).text
    
    #bs 이용
    soup = bs(response,'html.parser')
    
    #네이버 웹툰 페이지로 가서 원하는 정보의 위치 파악
    toons = []
    
    li = soup.select('.img_list li')
    for item in li:
        toon = {
            "title" : item.select_one('dt a')['title'],
            "url" : url_base + item.select('dt a')[0]['href'],
            "img_url" : item.select('.thumb img')[0]['src']
        }
        toons.append(toon)
    
    return render_template('naver_toon.html', t = toons)

@app.route('/daum_toon')
def daum_toon():
    #네이버 웹툰을 가져오는 URL 파악
    today = time.strftime("%a").lower()
    naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='+today
    url_base = 'https://comic.naver.com'
    
    #해당 주소로 요청을 보내 정보를 가져온다
    response = requests.get(naver_url).text
    
    #bs 이용
    soup = bs(response,'html.parser')
    
    #네이버 웹툰 페이지로 가서 원하는 정보의 위치 파악
    toons = []
    
    li = soup.select('.img_list li')
    for item in li:
        toon = {
            "title" : item.select_one('dt a')['title'],
            "url" : item.select('dt a')[0]['href'],
            "img_url" : item.select('.thumb img')[0]['src']
        }
        toons.append(toon)
    return render_template('daum_toon.html')