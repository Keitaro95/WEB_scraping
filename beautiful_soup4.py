import requests
from bs4 import BeautifulSoup


def yahoo_title_url():
    url = 'https://www.yahoo.co.jp/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(elems[0].prettify()) でCSSタグを確認

    try:
        elems = soup.select('#Topics')
        # yahooのホーム画面に表示されているニュースのurlとタイトル
        # print(elems[0].a['href']) 1番目の記事urlのみ撮りたい場合
        # print(elems[0].a.span.string) 1番目の記事タイトルのみ取りたい場合
        for sibling in elems[0].li.next_siblings:
            print(sibling.a['href'])
            print(sibling.a.span.string)
    except:
        elems = soup.select("#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul")
        elems = elems[0].find_all('li')
        for elem in elems:
            print(elem.a.span.string)
            print(elem.a['href'], end='\n\n')
    

# 詳細ページの中の「記事全文を表示」のリンクをゲットする関数
def yahoo_topcontent_url():
    url = 'https://www.yahoo.co.jp/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    elems = soup.select("#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul")
    elems = elems[0].find_all('li')
    pickup_links = [elem.a['href'] for elem in elems]

    news_links = []
    for pickup_link in pickup_links:
        pickup_res = requests.get(pickup_link)
        pickup_soup = BeautifulSoup(pickup_res.text, 'html.parser')
        pickup_elem = pickup_soup.find('p', class_='sc-cfteni')
        news_link = pickup_elem.a['href']
        news_links.append(news_link)

    print(news_links)