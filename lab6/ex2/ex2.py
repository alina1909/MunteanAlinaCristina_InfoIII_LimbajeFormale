import re

def generate_language(regex, limit=5):
    alphabet = 'abc'
    words = set()
    
    def generate_words(current, depth):
        if depth > limit:
            return
        if re.fullmatch(regex, current):
            words.add(current)
        for char in alphabet:
            generate_words(current + char, depth + 1)
    
    generate_words("", 0)
    return words

def union(lang1, lang2):
    return lang1 | lang2

def intersection(lang1, lang2):
    return lang1 & lang2

def concatenation(lang1, lang2):
    return {w1 + w2 for w1 in lang1 for w2 in lang2}

def substitution(lang, old, new):
    return {w.replace(old, new) for w in lang}

def inverse(lang):
    return {w[::-1] for w in lang}

def main():
    regex1 = input("Introduceti prima expresie regulata: ")
    regex2 = input("Introduceti a doua expresie regulata: ")
    
    lang1 = generate_language(regex1)
    lang2 = generate_language(regex2)
    
    while True:
        print("\nMeniu:")
        print("1. Reuniune")
        print("2. Intersectie")
        print("3. Concatenare")
        print("4. Substitutie")
        print("5. Invers")
        print("6. Iesire")
        
        choice = input("Alegeti o optiune: ")
        
        if choice == '1':
            print("\nReuniune:", union(lang1, lang2))
        elif choice == '2':
            print("\nIntersectie:", intersection(lang1, lang2))
        elif choice == '3':
            print("\nConcatenare:", concatenation(lang1, lang2))
        elif choice == '4':
            old = input("\nIntroduceti caracterul de inlocuit: ")
            new = input("Introduceti caracterul nou: ")
            print("Substitutie pentru prima expresie:", substitution(lang1, old, new))
            print("Substitutie pentru a doua expresie:", substitution(lang2, old, new))
        elif choice == '5':
            print("\nInvers pentru prima expresie:", inverse(lang1))
            print("Invers pentru a doua expresie:", inverse(lang2))
        elif choice == '6':
            print("Iesire...")
            break
        else:
            print("Optiune invalida. Incercati din nou.")

if __name__ == "__main__":
    main()
