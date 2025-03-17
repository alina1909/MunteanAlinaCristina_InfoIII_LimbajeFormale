class MealyTrafic:
    def __init__(self):
        self.state = "S0"
        self.tranzitii = {
            'S0': {'00': 'S0', '01': 'S1', '10': 'S0', '11': 'S1'},
            'S1': {'00': 'S1', '01': 'S1', '10': 'S0', '11': 'S0'}
        }
        self.output = {
            'S0': {'00': 0, '01': 1, '10': 0, '11': 1},
            'S1': {'00': 1, '01': 1, '10': 0, '11': 0}
        }
    
    def tranzitie(self, intrare):
        if intrare not in self.tranzitii[self.state]:
            print("Senzor a avut o eroare")
            return
        
        current_state = self.state
        self.state = self.tranzitii[self.state][intrare]
        iesire = self.output[self.state][intrare]
        print(f"{current_state} -> ({intrare}) = {self.state}, Iesire: {iesire}")
        
        if iesire == 0:
            print("A Verde, B Rosu")
        else:
            print("A Rosu, B Verde")
    
    def verificare(self):
        while True:
            intrare = input("\nIntroduceti semnalul (A, B) (ex: 00, 01, 10, 11) sau 'q' pentru a iesi: ").strip()
            if intrare == 'q':
                print("Ieșire...")
                break
            if intrare not in ['00', '01', '10', '11']:
                print("Input invalid")
                continue
            self.tranzitie(intrare)
    

if __name__ == "__main__":
    trafic = MealyTrafic()
    trafic.verificare()
