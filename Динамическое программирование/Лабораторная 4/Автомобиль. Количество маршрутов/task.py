from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    table_path = [[0] * m for _ in range(n)]

    table_path[0][0] = 1

    # Столбец
    for row_ind in range(n - 1):
        table_path[row_ind + 1][0] += table_path[row_ind][0]

    # Строка
    for col_ind in range(m - 1):
        table_path[0][col_ind + 1] += table_path[0][col_ind]

    # Диагональ
    for row_ind in range(n - 1):
        for col_ind in range(m - 1):
            table_path[row_ind + 1][col_ind + 1] += table_path[row_ind][col_ind]

    for i in range(1, n):
        for j in range(1, m):
            table_path[i][j] = table_path[i - 1][j] + table_path[i][j - 1] + table_path[i - 1][j - 1]
    return table_path


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
