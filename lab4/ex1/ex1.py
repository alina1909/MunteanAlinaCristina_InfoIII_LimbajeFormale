class NFAEpsilon:
    def __init__(self):
        self.states = {"q0", "q1", "q2", "q3", "q4"}
        self.start_state = "q0"
        self.final_states = {"q4"}
        
        self.tranzitii = {
            ("q0", "a"): {"q1"},
            ("q1", "a"): {"q1"},
            ("q1", "ε"): {"q2"},
            ("q2", "a"): {"q3"},
            ("q2", "b"): {"q2", "q3"},
            ("q3", "a"): {"q3"},
            ("q3", "b"): {"q1"},
            ("q3", "ε"): {"q4"}
        }

    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            if (state, "ε") in self.tranzitii:
                for next_state in self.tranzitii[(state, "ε")]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def verificare(self, secventa_intrari):
        current_states = self.epsilon_closure({self.start_state})
        print(f"Starea initiala: {current_states}")
        
        for litera in secventa_intrari:
            next_states = set()
            for state in current_states:
                if (state, litera) in self.tranzitii:
                    next_states.update(self.tranzitii[(state, litera)])
            current_states = self.epsilon_closure(next_states)
            print(f"Dupa intrarea '{litera}': {current_states}")
        
        accepted = any(state in self.final_states for state in current_states)
        print("Acceptat" if accepted else "Respins")




if __name__ == "__main__":
    nfa = NFAEpsilon()
    secventa_intrari = "aabbab"
    nfa.verificare(secventa_intrari)
