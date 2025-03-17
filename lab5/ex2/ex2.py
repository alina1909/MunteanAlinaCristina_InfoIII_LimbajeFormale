class NFA_Epsilon:
    def __init__(self):
        self.tranzitii = {
            'q0': {'ε': {'q1', 'q10'}},
            'q1': {'b': {'q2'}},
            'q2': {'ε': {'q3', 'q4'}},
            'q3': {'a': {'q5'}},
            'q4': {'b': {'q6'}},
            'q5': {'ε': {'q7'}},
            'q6': {'ε': {'q7'}},
            'q7': {'ε': {'q8'}},
            'q8': {'ε': {'q9'}},
            'q9': {'ε': {'q11', 'q17'}},
            'q10': {'a': {'q18'}},
            'q11': {'ε': {'q12', 'q13'}},
            'q12': {'a': {'q14'}},
            'q13': {'b': {'q15'}},
            'q14': {'ε': {'q16'}},
            'q15': {'ε': {'q16'}},
            'q16': {'ε': {'q11', 'q17'}},
            'q17': {'ε': {'q19'}},
            'q18': {'ε': {'q19'}},
            'q19': {'ε': {'q20'}},
            'q20': {}
        }
        self.start_state = 'q0'
        self.final_states = {'q20'}
    
    def epsilon(self, states):
        closure = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            for next_state in self.tranzitii.get(state, {}).get('ε', set()):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure
    
    def tranzitie(self, states, symbol):
        next_states = set()
        for state in states:
            next_states.update(self.tranzitii.get(state, {}).get(symbol, set()))
        return next_states
    
    def verificare(self, input_string):
        current_states = self.epsilon({self.start_state})
        print(f"Start: {current_states}")
        for simbol in input_string:
            next_states = self.tranzitie(current_states, simbol)
            current_states = self.epsilon(next_states)
            print(f"{simbol} -> {current_states}")
        
        if current_states & self.final_states:
            print(f"{input_string} apartine")
        else:
            print(f"{input_string} nu apartine")
    

if __name__ == "__main__":
    nfa = NFA_Epsilon()
    test_string = "babaaaaaba"
    nfa.verificare(test_string)
