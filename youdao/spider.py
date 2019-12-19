import execjs
import time,requests,json

with open(r'C:\Users\Administrator\Desktop\JS spider\youdao\fanyi.js','r',encoding='utf-8') as f:
    js = f.read()
ct = execjs.compile(js,cwd=r'C:\Users\Administrator\AppData\Roaming\npm\node_modules')
salt=ct.call('get_salt')
sign=ct.call('get_sign')
ts=int(time.time()*1000)


#_o要去掉，否则会出先error_code:50的报错
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
keyword=input("输入需要翻译的文字：")

headers = {
    'Cookie': '_ntes_nnid=6ac21e84865bd8e189722a733e5666e0,1573460916030; OUTFOX_SEARCH_USER_ID_NCOO=1782352705.7355099; OUTFOX_SEARCH_USER_ID=474078682@49.84.148.160; JSESSIONID=aaaQk6iD6hG8cfyQ4YB8w; ___rl__test__cookies={}'.format(int(time.time()*1000)),
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
data={
    'i':keyword,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':salt,
    'sign':sign,
    'ts':ts,
    'bv':'4aa7828b641c5e2587e46a4b35eb3523',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME'
}
response=requests.post(url,data=data,headers=headers)
result=json.loads(response.text)['translateResult'][0][0]['tgt']
print(result)
