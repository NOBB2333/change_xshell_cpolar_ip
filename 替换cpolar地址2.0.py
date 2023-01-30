# -*- coding: utf-8 -*-
import re
import requests

# -------------------配置信息------------------------------------------


# 文件路径
file_path = r"C:\Users\NOBB\Documents\NetSarang Computer\7\Xshell\Sessions\矿.cpolar.xsh"


# 正则的匹配信息
re_list = {
    # 替换cookie里最重要的 cf_bm 平时只会边这个
    "cookie_info":r'(?<=__cf_bm=).*?(?=;)',

    # 匹配登陆后网页ssh信息
    "ssh_info":r'(?<=ssh).*?(?=tr)',
    "ssh_port":r"(:\d{5})",
    "ssh_ip":r"([0-9]{1,2}.tcp.cpolar.[a-z]{1,3})",

    # 匹配文件中IP 和端口所在段落
    "file_ip":r'(Host=[0-9]{1,2}.tcp.cpolar.[a-z]{1,3})',
    "file_port":r'(Port=\d{5})',
}


# cookie
# cookie = "Hm_lvt_0838dad5461d14f63bdf207a43a54c29=1671014559; _ga=GA1.2.1292063761.1668412409; session=67ce1ba4-9fdf-4684-aae1-70c07559b566; _gid=GA1.2.115640722.1673237951; Hm_lpvt_0838dad5461d14f63bdf207a43a54c29=1673341442; __cf_bm=K1Ms0u5.cd4N1Zd0dr4DYIw.4NodmE_e1WBN5AU11Hg-1673341138-0-AWLcqeX0h2BTO2dssPsQhLhO9H9XcgdPRhURiE06260c0HIp6cW942QDfZ4mnfwrOHiOldhaBuFl3a0i3HqMBPq7vSvFLKJVm5wBatpWKM/X0pojMh74P45+Fj9SRfRRDjHYMr3Zr9jOxrL0bYlSCzc=; _gat_gtag_UA_128397857_1=1"
# cookie = "Hm_lvt_0838dad5461d14f63bdf207a43a54c29=1671014559; _ga=GA1.2.1292063761.1668412409; session=67ce1ba4-9fdf-4684-aae1-70c07559b566; _gid=GA1.2.115640722.1673237951; Hm_lpvt_0838dad5461d14f63bdf207a43a54c29=1673400920; __cf_bm=xLY1hyCInjOQrcCQq8T_LQyoX0HdfThXteNaeLxq3xk-1673400923-0-AR06VfjHxQwNfH09MgGN84pGk7nhUqIkY3oJ6vN+hsMpEhP3bfaLdEXEq6rGI9nR81RSael/N+53vIteX6FgAOkWlYHUGRHIbQWQ1lCCRXpqp62DYFSmDQ+ZBCr+nhSqwt3TLACLuElit8R9clqj1Pw=; _gat_gtag_UA_128397857_1=1",
cookie = "Hm_lvt_0838dad5461d14f63bdf207a43a54c29=1671014559; _ga=GA1.2.1292063761.1668412409; session=67ce1ba4-9fdf-4684-aae1-70c07559b566; _gid=GA1.2.115640722.1673237951; Hm_lpvt_0838dad5461d14f63bdf207a43a54c29=1673341442; __cf_bm={0}; _gat_gtag_UA_128397857_1=1"
cookie1 = "Hm_lvt_0838dad5461d14f63bdf207a43a54c29=1671014559; _ga=GA1.2.1292063761.1668412409; session=67ce1ba4-9fdf-4684-aae1-70c07559b566; _gid=GA1.2.115640722.1673237951; Hm_lpvt_0838dad5461d14f63bdf207a43a54c29=1673341442; {0}; _gat_gtag_UA_128397857_1=1"



user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# -------------------配置信息------------------------------------------




# 正则的匹配信息返回
def re_get(str, retext):
    pattern = re.compile(retext)
    return re.findall(pattern,str)




print("start")
# ------------------- 获取 set-cookie ------------------------------------------
# 匹配出 set cookie  只有新设备cookie失效后登录才会有setcookie
url = "https://dashboard.cpolar.com/cdn-cgi/challenge-platform/h/b/cv/result/7872c311a80fceb5"


session = requests.session()  # 使用 session 维持登陆状态
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/531.37 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

res = session.post(url)
cookie = requests.utils.dict_from_cookiejar(res.cookies)
cookie = session.post(url).headers['set-cookie']
print(cookie)

cookie = cookie1.format(cookie[0:154])
session.headers["Cookie"] = cookie
print(session.headers)
# -------------------信息解析------------------------------------------
url2 = "https://dashboard.cpolar.com/status"
# 请求参数
res = session.get(url2)
res = res.text.replace("\n","")
# print(res)
ssh_info =  re_get(res, re_list["ssh_info"])[0]

# 用正则匹配出来 IP 和 端口
ssh_ip =  re_get(ssh_info, re_list["ssh_ip"])[0]
ssh_port =  re_get(ssh_info, re_list["ssh_port"])[0][1::] # 这里多匹配了个冒号
print(ssh_port, ssh_ip)


# -------------------文件解析------------------------------------------


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