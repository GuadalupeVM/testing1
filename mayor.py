class Mayor:
    def __init__(self) -> None:
        pass

    def mayor(self, num1: int, num2: int) -> int or None:
        result = 0

        if num1 > num2:
            result = num1
        elif num2 > num1:
            result = num2
        else:
            return None
        return result
