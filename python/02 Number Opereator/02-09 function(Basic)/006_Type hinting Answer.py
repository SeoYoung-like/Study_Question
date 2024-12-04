# type hinting을 추가하시오.

def repeat_print(message: str = "안녕", count: int = 7) -> None:
    """message를 count번 출력"""

    for _ in range(count):
        print(message)


repeat_print(message=777)