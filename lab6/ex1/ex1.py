import itertools

def pump_lemma_check_L1(n):
    # L1={0^i 1^j | i>j}
    w = "0" * (n + 1) + "1" * n  
    for i in range(1, n + 1):  
        x = "0" * i
        y = "0"
        z = "0" * (n - i) + "1" * n
        pumped = x + y * 2 + z  
        count_0 = pumped.count("0")
        count_1 = pumped.count("1")
        if count_0 <= count_1:
            return False  
    return True

def pump_lemma_check_L2(n):
   # L2={a^i b^j | i<=j}
    w = "a" * n + "b" * n  
    for i in range(1, n + 1):
        x = "a" * i
        y = "a"
        z = "a" * (n - i) + "b" * n
        pumped = x + y * 2 + z  
        count_a = pumped.count("a")
        count_b = pumped.count("b")
        if count_a < count_b:
            return False  
    return True

def pump_lemma_check_L3(n):
    # L3={a^n b^n c^n | n>0}
    w = "a" * n + "b" * n + "c" * n  
    for i in range(1, n + 1):
        x = "a" * i
        y = "a"
        z = "a" * (n - i) + "b" * n + "c" * n
        pumped = x + y * 2 + z  
        count_a = pumped.count("a")
        count_b = pumped.count("b")
        count_c = pumped.count("c")
        if count_a != count_b or count_b != count_c:
            return True  
    return False

if __name__ == "__main__":
    n = 3 
    print(f"Limbajul 1 este regulat? {pump_lemma_check_L1(n) == False}")
    print(f"Limbajul 2 este regulat? {pump_lemma_check_L2(n) == False}")
    print(f"Limbajul 3 este regulat? {pump_lemma_check_L3(n) == False}")




