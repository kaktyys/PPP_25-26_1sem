def f(a):
    a = a.strip()
    if a.isdigit() or (a[0] == ('-') and a[1:].isdigit()):
        result = int(a)
        return result
    if a.startswith('(') and a.endswith(')'):
        count = 0
        for i, ch in enumerate(a):
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
            if count == 0 and i != len(a) - 1:
                break
        else:
            return f(a[1:-1])

    def ff(a, b):
        count = 0
        for i in range(len(a) - 1, -1, -1):
            ch = a[i]
            if ch == ')':
                count += 1
            elif ch == '(':
                count -= 1
            elif count == 0 and ch in b:
                return i
        return -1

    ind = ff(a, ['+', '-'])
    if ind != -1:
        first = a[:ind]
        second = a[ind + 1:]
        op = a[ind]
        first_v = f(first)
        second_v = f(second)
        if op == '+':
            result = first_v + second_v
        else:
            result = first_v - second_v
        print(f"{first_v} {op} {second_v} = {result}")
        return result

    ind = ff(a, ['*', '/'])
    if ind != -1:
        first = a[:ind]
        second = a[ind + 1:]
        op = a[ind]
        first_v = f(first)
        second_v = f(second)
        if op == '*':
            result = first_v * second_v
        else:
            result = first_v / second_v
        print(f"{first_v} {op} {second_v} = {result}")
        return result

    raise ValueError(f"Некорректное выражение: {a}")


# a = '9 - 4 + 2 * 5 - (4 / 2) * 3 - 14'
a = input()
print(f"Итоговый результат: {f(a)}")
