import requests

url = 'https://www.yahoo.co.jp/'

def requests_url_text(url, i):
    # response = requests.get(url)
    # response.status_code
    # response.content
    # response.text
    # response.encoding
    # response.cookies
    # for k,v in response.headers.items():
    #     print(k,':', v)

    #ユーザーエージェント確認サイト https://testpage.jp/tool/ip_user_agent.php を元に追加してください
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    #headerにuseragentを渡してリクエストが返ってくるようにする
    header = {"user-agent": user_agent}
    response = requests.get(url, headers=header, timeout=3)
    response.text[:i]


url = 'https://www.google.com/search'
def searchengine_queryword(url, word):
    #requestsを使ってサーチエンジンに検索語句を送ります
    # param = {'q': 'python'}
    param = {'q': word}
    response = requests.get(url, params=param)
    response.text