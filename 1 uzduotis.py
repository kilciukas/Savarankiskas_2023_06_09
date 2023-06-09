class BankoSaskaita:
    def __init__(self, saskaita, balansas):
        self.saskaita = saskaita
        self.balansas = balansas

    def prideti_pinigus(self, suma):
        teigiamas = abs(suma)
        self.balansas += teigiamas
        print(f'Sąskaita {self.saskaita} papildyta {teigiamas} EUR')

    def isimti_pinigus(self, suma):
        if suma > self.balansas:
            print(f"Iš sąskaitos {self.saskaita} išimti visi pinigai. Suma {self.balansas} EUR")
            self.balansas = 0
        else:
            if suma >= 0:
                neigiamas = suma * (-1)
                self.balansas += neigiamas
                print(f'Iš sąskaitos {self.saskaita} išimta {suma} EUR')
            else:
                self.balansas -= suma
                print(f'Iš sąskaitos {self.saskaita} išimta {suma} EUR')

    def spausdinti_balansa(self):
        print(f'Sąskaitos nr. {self.saskaita}, balansas = {self.balansas} EUR')

saskaita1 = BankoSaskaita("LT123456", 100)
saskaita1.prideti_pinigus(-1000)
saskaita1.isimti_pinigus(200)
saskaita1.spausdinti_balansa()
saskaita1.isimti_pinigus(500)
saskaita1.prideti_pinigus(200)
saskaita1.spausdinti_balansa()