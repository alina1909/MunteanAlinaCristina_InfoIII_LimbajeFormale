class Mealy:
    def __init__(self):
        self.state = "Q1"
        self.tranzitii = {
            ("Q1", "X"): ("Q2", "1"),
            ("Q1", "Y"): ("Q1", "1"),
            ("Q2", "X"): ("Q1", "2"),
            ("Q2", "Y"): ("Q2", "2"),
        }

    def verificare(self, secventa_intrari):
        secventa_iesiri = ""
        for litera in secventa_intrari:
            next_state, output = self.tranzitii.get((self.state, litera), (self.state, ""))
            print(f"{self.state} -> {litera} = {next_state}, Iesire: {output}")
            secventa_iesiri += output
            self.state = next_state

        print(f"Secventa iesirilor: {secventa_iesiri}")



if __name__ == "__main__":
    masina = Mealy()
    secventa_intrari = "XYXYX"
    masina.verificare(secventa_intrari)
