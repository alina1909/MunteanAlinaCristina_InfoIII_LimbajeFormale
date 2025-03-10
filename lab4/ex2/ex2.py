class Moore:
    def __init__(self):
        self.state = "S1"
        self.outputs = {"S1": "1", "S2": "2"}
        self.tranzitii = {
            ("S1", "A"): "S1",
            ("S1", "B"): "S2",
            ("S2", "A"): "S1",
            ("S2", "B"): "S2",
        }


    def verificare(self, secventa_intrari):
        secventa_iesiri = ""
        for litera in secventa_intrari:
            print(f"Stare: {self.state}, Iesire: {self.outputs[self.state]}, Intrare: {litera} ->")
            secventa_iesiri += self.outputs[self.state]
            self.state = self.tranzitii.get((self.state, litera), self.state)

        print(f"Stare finala: {self.state}, Iesire: {self.outputs[self.state]}")
        secventa_iesiri += self.outputs[self.state]
        print(f"Secventa iesirilor: {secventa_iesiri}")



if __name__ == "__main__":
    masina = Moore()
    secventa_intrari = "ABABBA"
    masina.verificare(secventa_intrari)
