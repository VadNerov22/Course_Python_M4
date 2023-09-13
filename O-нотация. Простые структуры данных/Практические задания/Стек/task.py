from typing import Any


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, elem: Any) -> None:
        """
        Добавление элемента в вершину стека

        :param elem: Элемент, который должен быть добавлен
        """
        self._stack.append(elem)

    def pop(self) -> Any:
        """
        Извлечение элемента из вершины стека.

        :raise: IndexError - Ошибка, если стек пуст

        :return: Извлеченный с вершины стека элемент.
        """
        if not self._stack:
            raise IndexError("Стек пуст")

        return self._stack.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в стеке, без его извлечения.

        :param ind: индекс элемента (отсчет с вершины, 0 - вершина, последний добавленный элемент, 1 - предпоследний элемент, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ стека

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Указан не целочисленный тип индекса")

        if not -1 < ind < len(self._stack):
            raise IndexError("Индекс вне границ стека")

        return self._stack[-1 - ind]

    def clear(self) -> None:
        """ Очистка стека. """
        self._stack.clear()

    def __len__(self) -> int:
        """ Количество элементов в стеке. """
        return len(self._stack)
