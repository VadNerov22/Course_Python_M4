"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError("Массив не должен быть пустым!")
    min_value = arr[0] # начальное значение
    min_index_value = [0] # индекс начального значения

    for i in range(len(arr)):
        if not isinstance(arr[i], int):
            raise TypeError("Массив должен состоять из целых чисел!")
        if arr[i] < min_value:
            min_index_value.clear()
            min_index_value.append(i)
            min_value = arr[i]

    return min_index_value[0]


if __name__ == "__main__":
    print(min_search([2, 7, 22, 1, 15, 89, 3, 1])) #3
    print(min_search([1, 1, 85, 1, 1, 1, 1, -1])) #7
    print(min_search(["n"]))
    print(min_search([]))
