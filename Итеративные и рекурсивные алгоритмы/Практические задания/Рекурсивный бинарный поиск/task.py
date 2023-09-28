from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    if right_border is None:
        right_border = len(seq) - 1

    if left_border > right_border:
        raise ValueError(f"Искомого элемента {value} нет в массиве")

    middle_index = left_border + (right_border - left_border) // 2
    middle_value = seq[middle_index]
    if value == middle_value:
        while True:
            if not 0 <= middle_index - 1 < len(seq) or seq[middle_index - 1] != value:
                break
            else:
                middle_index -= 1
        return middle_index
    elif middle_value > value:
        right_border = middle_index - 1
    else:
        left_border = middle_index + 1

    return binary_search(value, seq, left_border, right_border)
