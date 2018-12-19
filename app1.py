import requests
import time
from bs4 import BeautifulSoup as bs


##내가한거##
#네이버 웹툰을 가져오는 URL 파악
today = time.strftime("%a").lower()
naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='+today
url_base = 'https://comic.naver.com'


#해당 주소로 요청을 보내 정보를 가져온다
response = requests.get(naver_url).text

#bs 이용
soup = bs(response,'html.parser')

#네이버 웹툰 페이지로 가서 원하는 정보의 위치 파악
li = soup.select('.img_list li')
for item in li:
    title = item.select_one('dt a')['title']
    url = item.select('dt a')[0]['href']
    img_url = item.select('.thumb img')[0]['src']
    print(title,":", url_base+url)