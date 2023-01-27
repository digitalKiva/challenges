def func(input):
    found = {}
    res = ""
    for c in input:
        if not found[c]:
            found[c] = 1
        else:
            found[c] = found[c] + 1

    for k, v in found:
        if v > 1:
            res = res + k

    return res
