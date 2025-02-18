def generare_strings_rec(curent, rezultate):
    if len(curent) > 4:
        return
    rezultate.append(curent)
    generare_strings_rec(curent + "a", rezultate)
    generare_strings_rec(curent + "b", rezultate)


def generare_strings():
    rezultate = []
    generare_strings_rec( "", rezultate)
    return rezultate


strings = generare_strings()
print(" ".join(strings))
