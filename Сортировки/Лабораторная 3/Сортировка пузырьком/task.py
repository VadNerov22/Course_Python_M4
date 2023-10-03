from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container

    if len(container) == 1:
        return container

    for i in range(0, len(container) - 1):
        sorted = False # флаг на отслеживание перестановки в массиве
        for j in range(len(container) - i - 1):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]
                sorted = True

        if not sorted:
            return container


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(my_list)
    sort(my_list)
    print(my_list)
    my_list_1 = [3, 9, 5, 6, 8, 10, 2, 4, 7, 1]
    print(my_list_1)
    sort(my_list_1)
    print(my_list_1)
