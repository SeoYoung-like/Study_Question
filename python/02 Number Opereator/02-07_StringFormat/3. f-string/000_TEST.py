# 앞에 느낌표를 붙여서 주피터 노트북에서도 패키지 설치를 할 수 있습니다.
# 알파벳 외의 글자들이 적절한 크기를 가질 수 있게 조절하는 함수를 사용한다.
#!pip install wcwidth

from wcwidth import wcswidth

print(wcswidth("안녕AB"), len("안녕AB"))

def wcpadding(s, l):
    return s + " "*(l-wcswidth(s))

print(wcswidth("첫 번째 단어"))

# 스크립트 모드의 터미널 출력에서는 정확하게 줄맞춤 가능
print("{0}|{1}".format(wcpadding("첫 번째 단어", 12), wcpadding("두 번째 단어", 12)))
print("{0}|{1}".format(wcpadding("셋째", 12), wcpadding("넷째", 12)))

# 정확하게 줄맞춤이 가능하지만 불필요한 공백이 삽입 
# 주피터 노트북에서도 정상 작동을 할 수 있게, tab을 넣어준다.
print("{0}\t|{1}".format(wcpadding("첫 번째 단어", 12), wcpadding("두 번째 단어", 12)))
print("{0}\t|{1}".format(wcpadding("셋째", 12), wcpadding("넷째", 12)))