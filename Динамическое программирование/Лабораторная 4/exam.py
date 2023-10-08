"""
1. Задание
    - сложность цикла while логарифмическая O(log(n)) т.к. на каждом шаге размер входных данных
уменьшатеся в 1.7 раза
    - сложность merge_sort (сортировки слияния) O(nlog(n))
Таким образом сложность представленного алгоритма O(nlog(n))
"""

# 2. Задание
def counting_out(n: int, k: int) -> int:
    """
    Считалочка, игра происходит до тех пор, пока не останется последний человек.
    :param n: Количество человек.
    :param k: Количество слогов в считалке.
    :return: Выводит номер последнего оставшегося человка.
    """
    # Проверка вводимых данных
    if not isinstance(n, int):
        raise TypeError("Количество людей должно быть целым числом!")
    if n < 2:
        raise ValueError("Количество людей должно быть больше 1")

    if not isinstance(k, int):
        raise TypeError("Количество слогов должно быть целым числом!")
    if n <= 0:
        raise ValueError("Количество слогов в считалке должно быть больше 0!")

    result_ = 0

    for i in range(1, n + 1):
        result_ = (result_ + k) % i

    return (result_ + 1)


# 3. Задание
from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет подсчет компонентов связанности из стартового узла.
    :param g: Граф NetworkX, по которому нужно совершить обход.
    :param start_node: Стартовый узел, откуда нужно начать обход.
    :return: Число компонентов свзянности из стартового узла.
    """
    visited = {node: False for node in g.nodes}
    path = []

    def rec_dfs(current_node):
        visited[current_node] = True
        path.append(current_node)
        for neighbor in g[current_node]:
            if not visited[neighbor]:
                rec_dfs(neighbor)
    rec_dfs(start_node)
    return f"Число компонент связанности из стартового узла '{start_node}' = {len(path) - 1}"


# 4. Задание
from typing import Sequence


def dna(container: Sequence[str]) -> str:
    """
    Создание консенсус-строки
    :param container: Список из строк одинаковой длины.
    :return: Возвращает консенсус-строку.
    """
    res = lambda i: max(i, key=i.count)
    print(f"'{''.join(map(res, zip(*container)))}'")


# 5. Задание
from typing import List


def path_coasts(table: List[List[int]], start: List[List[int]], finish: List[List[int]],) -> List[List[int]]:
    """
    Расчет минимальной стоимости маршрутов до каждой клетки с учетом возможных перемещений.
    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё.
    :param start, finish: Координаты точки начала и окончания пути.
    :return: Возвращает таблицу минимальной стоимости перемещения по клеткам.
    """
    n = len(table) # количество строк
    m = len(table[0]) # количество столбцов
    res = [[0 for _ in range(m)] for _ in range(n)]

    n1 = start[0]
    m1 = start[1]
    f1 = finish[0]
    f2 = finish[1]
    path = [] # список путей

    res[n1][m1] = table[n1][m1]
    for i in range(1, f1 + 1):
        for j in range(1, f2 + 1):
            res[i][j] += min(res[i][j - 1], res[i - 1][j], res[i - 1][j - 1]) + table[i][j]

    i = f1
    j = f2
    while (i, j) >= (n1, m1):
        path.append((i, j))
        prev_res = min(res[i][j - 1], res[i - 1][j], res[i - 1][j - 1])
        if res[i][j - 1] == prev_res:
            i, j = i, j - 1
        elif res[i - 1][j] == prev_res:
            i, j = i - 1, j
        else:
            i, j = i - 1, j - 1
    path.append((n1, m1))
    return path[::-1]


if __name__ == "__main__":
    # Задача 2
    print(counting_out(10, 2)) # 5

    # Задача 3
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ("A", "B"),
        ("B", "A"),
        ("B", "C"),
        ("C", "B"),
        ("C", "D"),
        ("D", "C"),
        ("F", "G"),
        ("G", "F"),
    ])
    print(dfs(graph, "A")) # 3

    # Задача 4
    my_dna = [
        "ATTA",
        "ACTA",
        "AGCA",
        "ACAA"
        "BCTB"
    ]
    dna(my_dna) # 'ACTA'

    # Задача 5
    coasts_ceil = [
        [2, 7, 1, 3],
        [12, 4, 3, 9],
        [1, 5, 8, 5]
    ]
    total_coasts = path_coasts(coasts_ceil, [0, 1], [2, 3])
    print(total_coasts) # [(0, 1), (0, 2), (1, 2), (2, 3)]