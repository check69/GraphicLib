from typing import Union

def method1(x: int = 5, y: bool = True) -> Union[int, bool]:
    if y:
        return x

    return False

def method2() -> list:
    return [1, 2, 3]