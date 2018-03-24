# -*- coding: UTF-8 -*-
import urllib.request
from urllib import request
from lxml import etree
import random
import time
import chardet

#随机伪造header信息
def randHeader():
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0']

    header = {'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]}
    return header

# print(randHeader())
print("提示：\n\000\000\000\000关键词格式为：paper+machine+pdf+design\n\000\000\000\000必须存在的关键词:pdf\n\s000\000\000\000如需查询更多xpath结构的数据，请修改代码中的xpath表达式！")
keywords=input("请输入要查询关键词：")#动态获取输入的指


num_url=0
num_title=0
n=0
length_url=0
length_title=0
while n!=10:
    print(n)
    url='https://www.google.com.hk/search?q='+str(keywords)+'&num=50&safe=strict&biw=824&bih=561&ei=MFqVWuyJG8iijwT8g56oCw&start='+str(n*50)+'&sa=N'
    #headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req =request.Request(url=url, headers=randHeader())
    f=urllib.request.urlopen(req)
    response=f.read(300000)
    if response:
        html = etree.HTML(response)
        value_url=html.xpath("//span[@class='_ogd b w xsm']/../a/@href")
        value_title=html.xpath("//span[@class='_ogd b w xsm']/../a/text()")
        print('url'+str(value_url))
        print('title'+str(value_title))
        length_url+=len(value_url)
        length_title=len(value_title)
        with open("url.txt", "a") as f:  # 格式化字符串还能这么用！
            for key in value_url:
                num_url+=1
                f.write(str(num_url)+":"+str(key) + "\r\n")
                #f.write(etree.tostring(key).decode()+"\r\n")

        with open("title.txt", "a") as f:  # 格式化字符串还能这么用！
            for i in value_title:
                num_title+=1
                try:
                    f.write(str(num_title)+":"+str(i) + "<br/>\r\n")
                except:
                    print('该处由于字符编码格式不一致而出错，请手动添加...')
                    print(str(num_title)+":"+i)
        print('url'+str(length_url))
        print('title'+str(length_title))
        n+=1
        #time.sleep(5*(random.random()))         #间隔随机时间爬取页面
    else:
        n=10
print('总共数据条数约：'+str(length_url))
input()