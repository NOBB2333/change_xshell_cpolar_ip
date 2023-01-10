# -*- coding: utf-8 -*-
import re
import requests


# 正则的匹配信息返回
def re_get(str, retext):
    pattern = re.compile(retext)
    return re.findall(pattern,str)


# 正则的匹配信息
re_list = {
    # 替换cookie里最重要的数据
    "cookie_info":r'(?<=__cf_bm=).*?(?=;)',

    # 匹配登陆后网页ssh信息
    "ssh_info":r'(?<=ssh).*?(?=tr)',
    "ssh_port":r"(:\d{5})",
    "ssh_ip":r"([0-9]{1,2}.tcp.cpolar.[a-z]{1,3})",

    # 匹配文件中IP 和端口所在段落
    "file_ip":r'(Host=[0-9]{1,2}.tcp.cpolar.[a-z]{1,3})',
    "file_port":r'(Port=\d{5})',
}


print(1)
# -------------------登录页面------------------------------------------
url = "https://dashboard.cpolar.com/login"

params = {
"login": "2855813844@qq.com",
"password": "qqq111...",
"csrf_token": "1538662349.68##b5aa35f374452a6198004dab20d88b13583c7c2c"
}

headers = {
# ":authority": "dashboard.cpolar.com",
# ":method": "POST",
# ":path": "/login",
# ":scheme": "https",
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'content-length': '112',
'content-type': 'application/x-www-form-urlencoded',
# 'cookie': 'session=05a82cc6-1e18-44d9-bb0d-f7731205775a; Hm_lvt_0838dad5461d14f63bdf207a43a54c29=1673257698; __cf_bm=347Ro0MpVyZpddgWi25dZlxC2CLwWAkSI_HrO7rNcW4-1673257699-0-AQAUFx1pANAyKUGPsGXy3eYh67+i7ki8UdZBfsh2tjzAt3kqqzH9dkw+zqWbKWmFKPXxlb9wZDPr26ucEUthT6EryALBC0pdc0a3vCDD0mUeTN6bfJh2Traz+A11cfCCPW3h6V5hjbWrYDTVHa3dqvw=; _ga=GA1.2.2143066567.1673257706; _gid=GA1.2.658307697.1673257706; Hm_lpvt_0838dad5461d14f63bdf207a43a54c29=1673258034',
'origin': 'https//dashboard.cpolar.com',
'referer': 'https//dashboard.cpolar.com/login',
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',

}
"""
requests.post(url,data).headers['set-cookie']的方法，确实得到了USER_SESSION值，但得到的是一个字符串格式。在发送评论request请求的时候，要求参数cookie必须是json格式
链接：https://www.jianshu.com/p/0d79d4b5de33
"""
# session = requests.Session()
# cookie_jar = requests.post(url,data=params, headers=headers).cookies
# cookie = requests.utils.dict_from_cookiejar(cookie_jar)


# cookie = session.post(url,data=params, headers=headers).headers['set-cookie']
# print(cookie)





# 匹配出 set cookie  只有新设备cookie失效后登录才会有setcookie
# url = "https://dashboard.cpolar.com/cdn-cgi/challenge-platform/h/b/cv/result/7872c311a80fceb5"
# headers = {
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',

# }
# # 请求参数
# res = requests.post(url, headers=headers)
# cookie_info =  re_get(str(res.headers), re_list["cookie_info"])[0]
# print(cookie_info)


# -------------------信息解析------------------------------------------


url = "https://dashboard.cpolar.com/status"
headers = {
"Cookie":"Hm_lvt_0838dad5461d14f63bdf207a43a54c29=1671014559; _ga=GA1.2.1292063761.1668412409; session=67ce1ba4-9fdf-4684-aae1-70c07559b566; _gid=GA1.2.115640722.1673237951; Hm_lpvt_0838dad5461d14f63bdf207a43a54c29=1673327086; __cf_bm=gOT1lUyUve6P6OK3Gw7bxpmsZjhK8vDMW5VsliRK5hw-1673327088-0-AbNh8aEkXeH4MjaOKIPEE/DcQrbHtCFcd15kZvE9Karnz4fIUTYx9a4sN56Hhg6j9LdxHBocsTwQU904YA5/3MZzPC1NzXYMo9R6TstmpzbcdZJf2Rd0ntsYTLl/ILwFTz9Ts1+oELwlUkuQDSi7DYw=; _gat_gtag_UA_128397857_1=1;",
"Cookie":"Hm_lvt_0838dad5461d14f63bdf207a43a54c29=1671014559; _ga=GA1.2.1292063761.1668412409; session=67ce1ba4-9fdf-4684-aae1-70c07559b566; _gid=GA1.2.115640722.1673237951; Hm_lpvt_0838dad5461d14f63bdf207a43a54c29=1673341442; __cf_bm=K1Ms0u5.cd4N1Zd0dr4DYIw.4NodmE_e1WBN5AU11Hg-1673341138-0-AWLcqeX0h2BTO2dssPsQhLhO9H9XcgdPRhURiE06260c0HIp6cW942QDfZ4mnfwrOHiOldhaBuFl3a0i3HqMBPq7vSvFLKJVm5wBatpWKM/X0pojMh74P45+Fj9SRfRRDjHYMr3Zr9jOxrL0bYlSCzc=; _gat_gtag_UA_128397857_1=1",

'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',

}
# 请求参数
res = requests.get(url, headers=headers)
res = res.text.replace("\n","")
# print(res)
ssh_info =  re_get(res, re_list["ssh_info"])[0]

# 用正则匹配出来 IP 和 端口
ssh_ip =  re_get(ssh_info, re_list["ssh_ip"])[0]
ssh_port =  re_get(ssh_info, re_list["ssh_port"])[0][1::]
print(ssh_port, ssh_ip)


# -------------------文件解析------------------------------------------
# 文件路径
file_path = r"C:\Users\NOBB\Documents\NetSarang Computer\7\Xshell\Sessions\矿.cpolar.xsh"

# 读取数据 utf-16 格式
with open(file_path, "r", encoding="utf-16") as f:
    # f=open(file_path, encoding='utf-16')
    txt=""
    for line in f:
        txt+=line


# 匹配当前的
Host = re_get(txt, re_list["file_ip"])[0]
port = re_get(txt, re_list["file_port"])[0]

# 替换最新的
txt = txt.replace(Host, f"Host={ssh_ip}")
txt = txt.replace(port, f"Port={ssh_port}")

print(Host, port)
# print(txt )


# 写回文件
with open(file_path,"w",encoding="utf-16") as f:
    f.write(txt)