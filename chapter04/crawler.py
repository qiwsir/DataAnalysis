import requests
from lxml import etree
import time
import json
import re
import csv

headers = {
    'Cookie':'ipLoc-djd=1-72-2799-0; unpl=V2_ZzNtbRZXF0dwChEEfxtbV2IKFQ4RUBcSdg1PVSgZCVAyCkBVclRCFXMUR1NnGFkUZgoZXkpcQxNFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VH4RWAVmBxVeS19AEHUJR1x6GFsBYQEibUVncyVyDkBQehFsBFcCIh8WC0QcdQ1GUTYZWQ1jAxNZRVRKHXYNRlV6EV0EYAcUX3JWcxY%3d; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_e1ec43fa536c486bb6e62480b1ddd8c9|1496536177759; mt_xid=V2_52007VwMXWllYU14YShBUBmIDE1NVWVNdG08bbFZiURQBWgxaRkhKEQgZYgNFV0FRVFtIVUlbV2FTRgJcWVNcSHkaXQVhHxNVQVlXSx5BEl0DbAMaYl9oUmofSB9eB2YGElBtWFdcGA%3D%3D; __jda=122270672.14951056289241009006573.1495105629.1496491774.1496535400.5; __jdb=122270672.26.14951056289241009006573|5.1496535400; __jdc=122270672; 3AB9D23F7A4B3C9B=EJMY3ATK7HCS7VQQNJETFIMV7BZ5NCCCCSWL3UZVSJBDWJP3REWXTFXZ7O2CDKMGP6JJK7E5G4XXBH7UA32GN7EVRY; __jdu=14951056289241009006573',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

fp = open('/home/qiwsir/Documents/data_analysis/chapter04/bra2.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(fp)
#writer.writerow(('content','creationTime','productColor','productSize','userClientShow','userLevelName'))
writer.writerow(('creationTime','productColor','productSize'))

def get_id(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="gl-warp clearfix"]/li')
    for info in infos:
        try:
            id = info.xpath('@data-sku')[0]
            comment_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv6&productId={}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'.format(id)
            get_comment_info(comment_url,id)
        except IndexError:
            pass

def get_comment_info(url,id):
    html = requests.get(url,headers=headers)
    t = re.findall('fetchJSON_comment98vv6\((.*)\);', html.text)
    json_data = json.loads(t[0])
    page = json_data['maxPage']
    urls = ['https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv6&productId=%s&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(str(i)) for i in range(0,int(page))]
    for path in urls:
        html1 = requests.get(path%id, headers=headers)
        t1 = re.findall('fetchJSON_comment98vv6\((.*)\);', html1.text)
        json_data = json.loads(t1[0])
        for comment in json_data['comments']:
            #content = comment['content']
            creationTime = comment['creationTime']
            productColor = comment['productColor']
            productSize = comment['productSize']
            #userClientShow = comment['userClientShow']
            #userLevelName = comment['userLevelName']
            # print(content,creationTime,productColor,productSize,userClientShow,userLevelName)
            #writer.writerow((content,creationTime,productColor,productSize,userClientShow,userLevelName))
            writer.writerow((creationTime,productColor,productSize))
        time.sleep(2)

if __name__ == '__main__':
    url = "https://search.jd.com/Search?keyword=%E6%96%87%E8%83%B8&enc=utf-8&suggest=1.def.0.V14&wq=wen%27xiong&pvid=ddadea78ff104ef6924d1444cdeaaf41"
    #url = 'https://search.jd.com/Search?keyword=%E6%96%87%E8%83%B8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.his.0.0&page=1&s=1&click=0'
    get_id(url)
