def s1concat2(s1, s2):
    return s2 + s1


def s_la_n(s, n):
    return s * n


def reverse(s):
    return s[::-1]


def extract(s, i, j):
    return s[i:j+1]


def replace(s, sub, new_sub):
    return s.replace(sub, new_sub)


s = "ab12x1"

print("Concatenare:", s1concat2(s, "x5"))
print("Repetare:", s_la_n(s, 3))
print("Inversare:", reverse(s))
print("Extracție:", extract(s, 1, 4))
print("Înlocuire:", replace(s, "x1", "y4"))