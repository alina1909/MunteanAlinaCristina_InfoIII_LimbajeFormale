state = 'q0'
alfabet = {'C', 'T', 'A', 'H', 'OK'}

while True:
   
    if state == 'q0':
        print("\nAlege o bautura: (C)afea, (T)ea, C(A)ppuccino, (H)ot chocolate")
    elif state in {'q1', 'q2', 'q3'}:
        print("\nPentru confirmare introduce OK")
    elif state == 'q4':
        print("\nPentru finalizare comanda introduce OK")
    
    simbol = input("Optiune: ").strip().upper()
    
    if simbol not in alfabet:
        print("Selectie invalida! Incercati din nou.")
        continue
    
    if state == 'q0':
        if simbol == 'C':
            state = 'q1'
        elif simbol == 'T':
            state = 'q2'
        elif simbol == 'A':
            state = 'q3'
        elif simbol == 'H':
            state = 'q4'
    elif state in {'q1', 'q2', 'q3'} and simbol == 'OK':
        state = 'q4'
    elif state == 'q4':
        if simbol == 'OK':
            state = 'q0'
    else:
        print("Tranzitie invalida! Incercati din nou.")






