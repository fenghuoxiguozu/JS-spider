import execjs
import requests
import json

with open(r'C:\Users\Administrator\Desktop\JS spider\baidu\sign.js','r',encoding='utf-8') as f:
    js = f.read()
ct=execjs.compile(js)
sign=ct.call('e',"企业")

keyword=input("请输入要翻译的文字：")
url='https://fanyi.baidu.com/v2transapi?from=zh&to=en'

headers={
    'cookie': 'BIDUPSID=AAED24F267C9B6281A6B10903F779CFA; PSTM=1573306218; BAIDUID=AAED24F267C9B628C5C0E13CD57AFF49:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=3o5MWpuOFNKMkZVcHU1RFQyQjlLcjVtZ3N0Nk80d1BNM3RrZVNjblZNcy1HUkJlSVFBQUFBJCQAAAAAAAAAAAEAAABI7rY0t-m78M-3ufrX4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD6M6F0-jOhdb; APPGUIDE_8_2_2=1; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; MCITY=-%3A; H_PS_PSSID=1469_21080_30211_30284_22160; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; __yjsv5_shitong=1.0_7_c4d2a8802f1b93a258690ea55bafe67b853e_300_1577083773490_114.219.23.47_77ecdbc2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1575595834,1576466732,1577083522,1577083775; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1577083775; yjs_js_security_passport=e17e11ca1b13d262e3e6e532a861c1228d561a19_1577083774_js; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
}
data={
    'from':'zh',
    'to':'en',
    'query':keyword,
    'transtype':'translang',
    'simple_means_flag':'3',
    'sign':sign,
    'token':'cd0871c88b7b119d6f021481a2bc6f0e'
}
response=requests.post(url=url,data=data,headers=headers)
json_data=json.loads(response.text)
result=json_data['trans_result']['data'][0]['dst']
print(result)