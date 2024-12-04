def repeat_print(message="안녕", count=1):
    """message를 count번 출력"""

    for _ in range(count):
        print(message)


# 사용자의 의도와 다르게 작동하더라도 미리 확인하기가 어렵습니다.
repeat_print(count=3)