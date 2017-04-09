#encoding:utf-8
from bs4 import BeautifulSoup
import time,re,urllib2
import sys,csv


reload(sys)
sys.setdefaultencoding('utf-8')

websiteurls={}

def scanpage(url,papes,papelast):

    for k in range(1,papes):
        # print("这是第{}页".format(k))
        req = urllib2.Request(url+str(k)+papelast)
        websiteurl=req
        n=0
        html=urllib2.urlopen(websiteurl).read()
        soup = BeautifulSoup(html,"lxml")
        list1=[]
        list2=[]
        data=[]
        #写入csv
        csvfile = file('caiji05.csv', 'ab+')
        writer = csv.writer(csvfile)

        for hrefs in soup.find_all('a',href=re.compile(r"http://news.sina.com.cn/s/")):
            list1.append(hrefs.get('href'))
            list2.append(hrefs.string)
            print(hrefs.get('href'))
            print(hrefs.string)
            n +=1
        for hrefs in soup.find_all('a',href=re.compile(r"http://news.sina.com.cn/o/")):
            list1.append(hrefs.get('href'))
            list2.append(hrefs.string)
            print(hrefs.get('href'))
            print(hrefs.string)
            n +=1
        for hrefs in soup.find_all('a',href=re.compile(r"http://news.sina.com.cn/c/")):
            list1.append(hrefs.get('href'))
            list2.append(hrefs.string)
            print(hrefs.get('href'))
            print(hrefs.string)
            n +=1
        for i in range(0,n):
            data.append((list1[i],list2[i]))
        writer.writerows(data)
        csvfile.close()
        # time.sleep(1)
        print("已采集了{}页".format(k))
        # print("获取的链接的数量：")
        # print(int(n))



if __name__ == '__main__':
    scanpage('http://roll.news.sina.com.cn/news/shxw/qwys/index_',100,'.shtml')
    scanpage('http://roll.news.sina.com.cn/news/shxw/zqsk/index_',100,'.shtml')
    scanpage('http://roll.news.sina.com.cn/news/shxw/fz-shyf/index_',100,'.shtml')
    scanpage('http://roll.news.sina.com.cn/news/shxw/shwx/index_',100,'.shtml')


