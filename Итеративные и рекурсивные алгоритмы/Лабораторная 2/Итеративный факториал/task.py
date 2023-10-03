def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):
        raise TypeError("Число, факториал которого нужно найти, должно быть целым!")
    if n < 0:
        raise ValueError("Число, факториал которого нужно найти, должно быть положительным!")

    f = 1  # факториал 1

    if n == 0:
        return 1
    if n == 1:
        return f

    for i in range(2, n + 1):
        f = i * f
    return f


if __name__ == "__main__":
    print(factorial_iterative(8)) #40320
