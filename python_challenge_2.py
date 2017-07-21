#-*- coding:utf8 -*-
import re,urllib

def main_url(url):
    u_open=urllib.urlopen(url)
    main_page = u_open.read()
    return main_page

problem = main_url('http://www.pythonchallenge.com/pc/def/ocr.html')
text = problem[problem.rindex('<!--'):problem.rindex('-->')]
findtext = re.findall("[A-Za-z]", text)
print "".join(findtext)


