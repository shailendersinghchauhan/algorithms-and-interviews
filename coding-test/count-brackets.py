def getmidpoint(string_passed):
    str_length = len(string_passed)
    openb = [None] * (str_length + 1)
    closeb = [None] * (str_length + 1)
    index = -1

    openb[0] = 0
    closeb[str_length] = 0

    if (string_passed[0] == '('):
        openb[1] = 1
    if (string_passed[str_length - 1] == ')'):
        closeb[str_length - 1] = 1

    for i in range(1, str_length):
        if (string_passed[i] == '('):
            openb[i + 1] = openb[i] + 1
        else:
            openb[i + 1] = openb[i]

    for i in range(str_length - 2, -1, -1):
        if (string_passed[i] == ')'):
            closeb[i] = closeb[i + 1] + 1
        else:
            closeb[i] = closeb[i + 1]

    if (openb[str_length] == 0):
        return len
    if (closeb[0] == 0):
        return 0

    for i in range(str_length + 1):
        if (openb[i] == closeb[i]):
            index = i

    return index


string_passed = "()"
print(getmidpoint(string_passed))