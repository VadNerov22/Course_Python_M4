from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container

    if len(container) == 1:
        return container

    arr_ = [0] * (max(container) + 1) # 1. Вспомогательный массив

    for i in range(len(container)): # 2. Количество каждого объекта
        arr_[container[i]] += 1

    result_arr = [0] * len(container) # 3. Восстанавливаем отсортированный массив
    n = 0

    for i in range(max(container) + 1):
        while arr_[i] != 0:
            result_arr[n] = i
            n += 1
            arr_[i] -= 1
    return result_arr


if __name__ == "__main__":
    my_list = sort([2, 2, 2, 8, 3, 3, 5, 7, 0, 1])
    print(my_list)
