# encoding=utf-8
import json
import base64
import requests
import chardet

"""
输入你的微博账号和密码，可去淘宝买，一元七个。
建议买几十个，微博限制的严，太频繁了会出现302转移。
或者你也可以把时间间隔调大点。
"""
url= 'http://weibo.com/u/3822958337/home?wvr=5'
myWeiBo = [
    {'no': '13650382718', 'psw': 'fafa1454447420'},
    # {'no': 'shudieful3618@163.com', 'psw': 'a123456'},
]


def getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
    for elem in weibo:
        account = elem['no']
        password = elem['psw']
        username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": username,
            "service": "sso",
            "sp": password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        session = requests.Session()
        # session.headers.update(
        #     {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3026.3 Safari/537.36"})
        r = session.post(loginURL, data=postData)
        jsonStr = r.content.decode('gbk')
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            print ("Get Cookie Success!( Account:%s )" % account)
            cookie = session.cookies.get_dict()
            cookies.append(cookie)
        else:
            print ("Failed!( Reason:%s )" % info['reason'])
    return cookies


cookie = getCookies(myWeiBo)[0]
html = requests.get(url = url,cookies=cookie).content
encod = chardet.detect(html)['encoding']
html = html.decode(encoding=encod)
print(html)
# print(cookies)
# print ("Get Cookies Finish!( Num:%d)" % len(cookies))
