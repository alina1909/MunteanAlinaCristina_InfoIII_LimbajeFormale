from itertools import permutations

Q = {"q0", "q1", "q2", "q3"}  
E = {"a", "b", "c", "d"} 
q0 = "q0"  
F = {"q3"}  

tranzitii = {
    ("q0", "a"): "q1",
    ("q0", "b"): "q0",
    ("q0", "c"): "q0",
    ("q0", "d"): "q0",
    ("q1", "a"): "q1",
    ("q1", "b"): "q2",
    ("q1", "c"): "q1",
    ("q1", "d"): "q1",
    ("q2", "a"): "q2",
    ("q2", "b"): "q2",
    ("q2", "c"): "q2",
    ("q2", "d"): "q3",
    ("q3", "a"): "q3",
    ("q3", "b"): "q3",
    ("q3", "c"): "q3",
    ("q3", "d"): "q3",
}

def verificare(word):
    if len(word) > 6:
        return False
    
    nr_litere = {char: word.count(char) for char in set(word)}
    litere_dublate = [char for char, count in nr_litere.items() if count == 2]
    
    return len(litere_dublate) == 3


all_words = ["".join(p) for p in permutations("aabbccdd", 6)]


valid_words = set(filter(verificare, all_words))

print("Cuvintele din limbajul L:")
for word in sorted(valid_words):
    print(word)


test_words = ["aabbcc", "aaa", "bbbaac"]
for word in test_words:
    print(f"Cuvantul '{word}' este in limbajul L? {'DA' if word in valid_words else 'NU'}")
