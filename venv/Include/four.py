import requests

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400'
}

re=requests.get(url='https://baike.sogou.com/v7219742.htm?fromTitle=%E7%99%BE%E5%BA%A6%E6%96%87%E5%BA%93',headers=headers)
code=re.status_code
print(code)
with open('./text.html','wb+') as f:
    f.write(re.text.encode('utf8'))