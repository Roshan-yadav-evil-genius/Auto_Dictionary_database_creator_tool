letters = "abcdefghijklmnopqrstuvwxyz"
Sl = [x for x in letters]
Sl.append(" ")
Cl = [x.upper() for x in letters]


def alphabate(value):
    value = [x for x in value]
    if value[0] in Sl or value[0] in Cl:
        return True
    return False


def RemoveAlphabate(data: str):
    data = [x for x in data]
    result = ""
    for x in data:
        if x not in Cl and x not in Sl:
            result += x
    return result


if __name__ == '__main__':
    print(eval(RemoveAlphabate("What is 5 + 2")))
