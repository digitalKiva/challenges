def returndups(input):
    found = {}
    res = ""
    for c in input:
        if not found.get(c):
            found[c] = 1
        else:
            found[c] = found[c] + 1

    for k, v in found.items():
        if v > 1:
            res = res + k

    return res

def main():
    assert(returndups("joseph") == "")
    assert(returndups("helloo") == "lo")
    assert(returndups("hhheeellloo") == "helo")
    assert(returndups("") == "")

if __name__ == "__main__":
    main()