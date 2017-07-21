#-*- coding:utf8 -*-
import re,urllib  #re,urllib 라이브러리 import

def main_url(url):   #main_url 함수 정의
    u_open=urllib.urlopen(url) #url 오픈
    main_page = u_open.read()  #페이지 소스를 읽어 main_page에 저장
    return main_page

problem = main_url('http://www.pythonchallenge.com/pc/def/ocr.html')  #문제 페이지 소스가 problem 변수에 저장
text = problem[problem.rindex('<!--'):problem.rindex('-->')] #rindex 함수를 이용해 "<!--", "-->" 문자의 인덱스 값을 구해 배열의 인덱스로 접근해 해당 인덱스 사이의 모든 문자인 특수문자의 조합을 뽑음
findtext = re.findall("[A-Za-z]", text) #re 라이브러리의 findall 기능을 이용해 대문자 A ~ Z, 소문자 a ~ z 에 매칭되는 모든 문자를 찾아 findtext 변수에 저장
print "".join(findtext)


