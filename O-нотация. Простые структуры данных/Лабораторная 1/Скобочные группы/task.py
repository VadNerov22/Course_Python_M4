def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок
    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    if not isinstance(brackets_row, str):
        return False
    if brackets_row == "":
        return True
    if list(brackets_row)[0] in ")]}" or list(brackets_row)[-1] in "([{":
        return False

    stack = []
    for i in brackets_row:
        if i in "([{}])":
            if i in "([{":
                stack.append(i)
            elif not stack:
                return False
            if i in ")]}":
                last = stack.pop()
                if (last == "(" and i != ")") or (last == "[" and i != "]") or \
                        (last == "{" and i != "}"):
                    return False

    if stack:
        return False
    return True


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
    print(check_brackets(" "))  # True
    print(check_brackets("((()))"))  # True
    print(check_brackets("((())), {}, []"))  # True
    print(check_brackets("(()()"))  # False
    print(check_brackets("({)(}"))  # False
    print(check_brackets(""))  # True
