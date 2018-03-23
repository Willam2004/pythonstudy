def Stone(J, S):
    c = 0
    for s in S:
        if s in J:
            c = c + 1
    return c


J = "z"
S = "ZZ"

c = Stone(J, S)
print(c)
