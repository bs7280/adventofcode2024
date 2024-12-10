def opperate(v1, v2, opp):
    """
    eq = (81, 40, '+')
    return total (in this case 121)
    """
    if opp == "+":
        return v1 + v2
    elif opp == "*":
        return v1 * v2
    elif opp == "||":
        return int(str(v1) + str(v2))
    else:
        raise ValueError("Invalid opperator")


def p1(data, operators=["+", "*"]):
    data = data.split("\n")

    totals = []
    for i, row in enumerate(data):
        total, vals = row.split(":")
        vals = [int(v) for v in vals.strip().split(" ")]
        total = int(total)
        print(total, vals)

        # Loop through combinations and apply + and * operators
        opps = ["+"] * (len(vals) - 1)

        import itertools
        import functools

        for opps in itertools.product(operators, repeat=len(vals) - 1):
            # print(opps)
            tree = list(zip(zip(vals, vals[1:]), opps))

            # devault vaule is +, because functools.reduce will start with 0
            # in the acc variable
            eq = list(zip(vals, ("+",) + opps))
            result = functools.reduce(lambda acc, v: opperate(acc, v[0], v[1]), eq, 0)

            if result == total:
                # print("Found")
                totals.append(total)
                break
    print(sum(totals))


def p2(data):
    p1(data, ["||", "+", "*"])


with open("data.txt", "r") as fh:
    data = fh.read()

p1(data)

p2(data)
