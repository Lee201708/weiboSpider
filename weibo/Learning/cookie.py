import requests
import chardet
from lxml import etree


# cook = {'Cookie' : 'SINAGLOBAL=5562282320166.825.1487744032927; YF-Ugrow-G0=ad83bc19c1269e709f753b172bddb094; login_sid_t=dd5a553a1acd08a3aebaf33b7f02429b; YF-V5-G0=5f9bd778c31f9e6f413e97a1d464047a; WBStorage=02e13baf68409715|undefined; _s_tentry=-; Apache=2289153207234.491.1490413693751; ULV=1490413693764:1:1:1:2289153207234.491.1490413693751:; SCF=ArbFi6gL_HHIxmKy_2SttdrPKCp6sv_65N6qec44e086HFf-5sRC7AD1YiaUsgRWh0PEijM30diU7IKLL6osrW8.; SUB=_2A2510ZiLDeRxGeVG6VAY9SbPyDuIHXVWpo1DrDV8PUNbmtBeLUfykW9TFgzY1SaV2p9Eui4M6WlNzpCfoQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWOv.CKrPGvcDhSlTo1v9i25JpX5K2hUgL.FoeReoz4SKn0e0M2dJLoI7UDPfve9gHk; SUHB=03o1r83retZa0A; ALF=1521949787; SSOLoginState=1490413788; un=13650382718; wvr=6'}
# urls = 'http://weibo.com/u/3822958337'
url = 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dwapv4%26tip%3D1'
url_login = 'http://login.weibo.cn/login/'

'''使用content 返回的是byte型的数据'''
html = requests.get(url = url).content
# encod = chardet.detect(html)['encoding']
# html = html.decode(encoding=encod)
# print(html)

# '''使用text 返回的是unicode字符串'''
# html = requests.get(url = urls).text
# print(html)

# #
selector = etree.HTML(html)
password = selector.xpath('//input[@type="password"]/@name')[0]
vk = selector.xpath('//input[@name="vk"]/@value')[0]
actions = selector.xpath('//form[@method="post"]/@action')[0]
# print(selector)
print(password)
print(vk)
print(actions)

new_url = url_login + actions
headers = {
    'User_Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

datas = {
    'mobile' : '13650382718',
    password : 'fafa1454447420',
    'remember' : 'on',
    'backURL' : urls,
    'tryConnt' : '',
    'vk' : vk,
    'submit' : u'登录'
}
#
newhtml = requests.post(new_url,header=headers,data=datas).content
print(newhtml)