def e_palindrom(s):
    return s == s[::-1]


def lista_palindroame(E, lungime, numar, rezultate):
    if len(numar) == lungime:
        if e_palindrom(numar):
            rezultate.append(numar)
        return
    
    for char in E:
        lista_palindroame(E, lungime, numar + char, rezultate)


def afisare_palindrome(E):
    E_lista = list(E)
    for lungime in range(1, 6):
        rezultate = []
        lista_palindroame(E_lista, lungime, "", rezultate)
        print(f" {lungime}: {rezultate}")

E = {'0', '1', '2'}

afisare_palindrome(E)

