"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        self.priority_queue: dict[int, deque] = {
            priority: deque() for priority in range(self.HIGH_PRIORITY,
                                                    self.LOW_PRIORITY + 1)}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        self.priority_queue[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        for queve in self.priority_queue.values():
            if queve:
                return queve.popleft()

        raise IndexError("Очередь пуста")

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Указан не целочисленный тип индекса")

        queue = self.priority_queue[priority]
        if not -1 < ind < len(queue):
            raise IndexError("Индекс вне границ очереди")

        return queue[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        for queve in self.priority_queue.values():
            queve.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        len_ = 0
        for queve in self.priority_queue.values():
            len_ += len(queve)
        return len_
