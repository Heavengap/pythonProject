import requests
from bs4 import BeautifulSoup
伪装 = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
url = "https://book.zongheng.com/showchapter/1209675.html"
res = requests.get(url, headers=伪装)
soup = BeautifulSoup(res.text, 'lxml')
lis = soup.find_all('li', class_='col-4')
for l in lis:
    a = l.find('a')
    地址 = a.get('href')
    标题 = a.get( 'title')
    print(a)
    print(标题,地址)
    res1 = requests.get(地址,headers=伪装)
    soup1 = BeautifulSoup(res1.text,'lxml')
    小说内容1=soup1.find_all('div',class_=('content'))[0]
    text='\n'.join(小说内容1.stripped_strings)
    open(f'九个师姐/{标题}.text','w').write(text)