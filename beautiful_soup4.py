import requests
from bs4 import BeautifulSoup


# yahooJapanのホーム画面に表示されているニュースのurlとタイトルを取得する関数です
def yahoo_title_url():
    url = 'https://www.yahoo.co.jp/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        elems = soup.select('#Topics') # 取得したい範囲を指定しています
        for sibling in elems[0].li.next_siblings:
            print(sibling.a['href'])
            print(sibling.a.span.string)
    except:
        elems = soup.select("#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul")
        elems = elems[0].find_all('li') # find_allでliタグを取得します
        for elem in elems:
            print(elem.a.span.string)
            print(elem.a['href'], end='\n\n')
    


def yahoo_topnews():
    url = 'https://www.yahoo.co.jp/' # urlを指定します
    res = requests.get(url) # requestsで情報を全部取得します
    soup = BeautifulSoup(res.text, 'html.parser') # text部分のみを取り出します
    elems = soup.select("#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul") # CSSセレクタで取り出します
    elems = elems[0].find_all('li') # 取り出した中からliタグを取得します
    pickup_links = [elem.a['href'] for elem in elems] # aタグのurlを取得します

    # 詳細ページの中の「記事全文を表示」のリンクを取得します
    news_links = []
    for pickup_link in pickup_links:
        pickup_res = requests.get(pickup_link)
        pickup_soup = BeautifulSoup(pickup_res.text, 'html.parser')
        pickup_elem = pickup_soup.find('p', class_='sc-cfteni') # クラスを指定してpタグを取ってきます
        news_link = pickup_elem.a['href'] # aタグの中にあるリンクを取ります
        news_links.append(news_link) #リストに追加します

    # print(news_links)
    
    # リンクに遷移して記事のタイトル, url, 本文を取り出します
    for news_link in news_links:
        article_url = news_link
        article_res = requests.get(article_url)
        article_soup = BeautifulSoup(article_res.text, 'html.parser')
        title = article_soup.title.string
        article_text = article_soup.find('p', class_="sc-cTsKDU")
        print(title)
        print(article_url)
        print(article_text.text if hasattr(article_text, 'text') else '', end='\n\n\n\n')