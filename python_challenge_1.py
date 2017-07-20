# #-*- coding:utf-8 -*-
__name__ = "이꼬깔"

problem = "해당문제 카이사르 암호문"
length = len(problem)    #len함수를 이용해 카이사르 암호문의 길이를 구하고 length 변수에 저장
for k in range(length):  #카이사르 암호문의 길이 수만큼 for문 수행
    try:
        decode = ord(problem[k])+2   #decode 변수에 카이사르 각 알파벳들을 ord 함수를 이용해 아스키 코드로 변환시켜 저장하고 그 값에 +2 를 하여 알파벳을 2칸 앞당김
        if decode >= ord("z"):       # "z"의 아스키값 122에 +2를 하게 되면 "|" 특수문자가 출력된다. 아스키값이 122와 같거나 크면 if문 수행
            rep_decode = decode-26   #아스키값이 122를 넘어가면 a의 아스키 코드 값인 97로 돌아간다음 +2 해줌
            print "".join(unichr(rep_decode)), #unichr 함수를 이용해 아스키 코드를 알파벳으로 변환
        elif decode <= ord("0"):     #마침표 "." 역시 치환되기 때문에 그것을 방지하기 위한 코드
            rep_decode = decode - 2
            print "".join(unichr(rep_decode)),
        else:
            print "".join(unichr(decode)), #아스키값들을 알파벳으로 출력
    except: pass
