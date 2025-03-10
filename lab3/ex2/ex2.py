loc = 5  
nr = 0 
s = {'q0'}  

tranzitii = {
    'q0': {'v': {'q1'},'e':{'q3'}}, 
    'q1': {'v': {'q1', 'q2'}, 'p': {'q0', 'q1'},'e':{'q3'}}, 
    'q2': {'p': {'q1'},'e':{'q3'}},
    'q3':{}
}

def tranzitie(simbol):
    global s
    new_s = set()
    for state in s:
        if simbol in tranzitii.get(state, {}):
            new_s.update(tranzitii[state][simbol]) 
    if new_s:
        s = new_s
    
    else:
        print("Eroare")

while True:
    print("\n\nState:", s)
    print("Nr curent masini:", nr)
    print("Alege o optiune: (v)ine, (p)leaca, (e)xit")
    action = input("Optiune: ").strip().lower()
    #print("\n\n")

    if action == 'v':
        if nr < loc:
            nr += 1
            tranzitie('v')
            if nr == loc:
                s = {'q2'} 
        else:
            print("\nParcare plina!")
    elif action == 'p':
        if nr > 0:
            nr -= 1
            tranzitie('p')  
            if nr == 0:
                s = {'q0'}  
        else:
            print("\nParcare goala!")
    elif action == 'e':
        tranzitie('e')
    else:
        print("\nInput gresit!")
    if s=={'q3'}:
        print("Exit")
        break
