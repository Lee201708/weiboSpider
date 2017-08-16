# encoding=utf-8
import json
import base64
import requests
import chardet


myWeiBo = [
    {'no': 'meiqiao0166451@163.com', 'psw': 'tttt5555'},
    {'no': 'p85017230taogu742@163.com', 'psw': 'tttt5555'},
    {'no': 'iuy42766840shahu@163.com', 'psw': 'tttt5555'},

    # {'no': 'shudieful3618@163.com', 'psw': 'a123456'},
]


def getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
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
        r = session.post(loginURL, data=postData)
        # print('r:',r)
        # print('r.status_code:',r.status_code)
        # print('r.header:',r.headers)
        # print('r.cookies:',r.cookies)
        # print('r.content:',r.content)
        jsonStr = r.content.decode('gbk')
        # print('jsonStr:',jsonStr)
        #将str 转换为 dict
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            print ("Get Cookie Success!( Account:%s )" % account)
            cookie = session.cookies.get_dict()
            cookies.append(cookie)
        else:
            print("Failed!(Account:{0} Reason:{1} )".format(account,info['reason']))
            # pass
    return cookies

cookies = getCookies(weibo=myWeiBo)



# if __name__ == '__main__':
#     getCookies(myWeiBo)