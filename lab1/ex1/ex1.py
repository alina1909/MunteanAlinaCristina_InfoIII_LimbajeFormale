def concatenare(s1, s2):
    return s1 + s2


def inversare(s):
    return s[::-1]


def substitutie(s, a, b):
    return s.replace(a, b)


def lungime(s):
    return len(s)


s1 = "abc"
s2 = "xyz"

print("Concatenare:", concatenare(s1, s2))
print("Inversare:", inversare(s1))
print("Substituție:", substitutie(s1, 'b', '2'))
print("Lungime:", lungime(s1))
