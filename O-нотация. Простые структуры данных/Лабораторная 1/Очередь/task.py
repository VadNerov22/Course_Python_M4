"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Отсчет с начала, 0 - первый с начала элемент в очереди,
        1 - второй с начала элемент в очереди, и т.д.
        """
        self._l_queue = []

    def enqueue(self, elem: Any) -> None: # O(1)
        """
        Добавление элемент в конец очереди
        :param elem: Элемент, который должен быть добавлен
        """
        self._l_queue.append(elem)

    def dequeue(self) -> Any: # O(1)
        """
        Извлечение элемента из начала очереди.
        :raise: IndexError - Ошибка, если очередь пуста
        :return: Извлеченный с начала очереди элемент.
        """
        if not self._l_queue:
            raise IndexError("Очередь пуста, нет элементов для извлечения!")

        return self._l_queue.pop(0)

    def peek(self, ind: int = 0) -> Any: # O(1)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.
        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)
        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди
        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Указан не целочисленный тип индекса!")

        if not -1 < ind < len(self._l_queue):
            raise IndexError("Индекс вне границ очереди!")

        return self._l_queue[ind]

    def clear(self) -> None: # O(1)
        """ Очистка очереди. """
        self._l_queue.clear()

    def __len__(self): # O(1)
        """ Количество элементов в очереди. """
        return len(self._l_queue)
