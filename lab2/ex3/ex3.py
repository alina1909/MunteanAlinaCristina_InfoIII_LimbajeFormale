class AutomatFinit:
    def __init__(self):
        self.states = {"q0", "q1", "q2", "q3"}
        self.alfabet = {"a", "b", "c", "d"}
        self.tranziti = {
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
            ("q3", "d"): "q3"
        }
        self.initial_state = "q0"
        self.final_states = {"q3"}
    
    def verificare(self, input_string):
        current_state = self.initial_state
        for simbol in input_string:
            if (current_state, simbol) in self.tranziti:
                current_state = self.tranziti[(current_state, simbol)]
            else:
                return False  
        return current_state in self.final_states



automat = AutomatFinit()
cuvinte = ["aabbdd", "aabbcc", "dbaabd"]

for cuvant in cuvinte:
    rezultat = automat.verificare(cuvant)
    print(f"Cuvantul '{cuvant}' este in limbajul L? {rezultat}")



