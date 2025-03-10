class NFA:
    def __init__(self):
        self.states = {"q0", "q1", "q2"}
        self.alfabet = {"0", "1", "2"}
        self.start_state = "q0"
        self.final_states = {"q2"}
        self.tranzitii = {
            "q0": {"0": {"q0", "q1", "q2"}, "1": {"q1", "q2"}, "2": {"q2"}},
            "q1": {"1": {"q1", "q2"}, "2": {"q2"}},
            "q2": {"2": {"q2"}}
        }
    
    def tranzitie(self, current_states, simbol):
        new_states = set()
        for state in current_states:
            if simbol in self.tranzitii.get(state, {}):
                new_states.update(self.tranzitii[state][simbol])
        return new_states
    
    def verificare(self, input_string):
        current_states = {self.start_state}
        for simbol in input_string:
            if simbol not in self.alfabet:
                print(f"Input invalid: {simbol}")
                return False
            current_states = self.tranzitie(current_states, simbol)
            print(f"Dupa '{simbol}', starile curente: {current_states}")
        
        return bool(current_states & self.final_states)


if __name__ == "__main__":
    nfa = NFA()
    input_string = input("Introduceti un sir de simboluri (0,1,2): ")
    accepted = nfa.verificare(input_string)
    if accepted:
        print("Sirul este acceptat de automat.")
    else:
        print("Sirul nu este acceptat de automat.")





