import urllib.request
import urllib.error
import urllib.parse
import ssl

headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0'
}

value = {'source': 'index_nav',
'form_password': 'guo18842620930',
'form_email': '18842620930'
}
#python2.79之后会引入ssl验证，下面为创建一个未经验证的ssl
context = ssl._create_unverified_context()
try:
    data = urllib.parse.urlencode(value).encode('utf8')
    response = urllib.request.Request('https://www.douban.com/login', data=data, headers=headers)
    html = urllib.request.urlopen(response,context=context)
    result = html.read().decode('utf8')
    print(result)
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('错误原因是' + str(e.reason))
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('错误编码是' + str(e.code))
else:
    print('请求成功通过。')
