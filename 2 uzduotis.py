class Figūra:
    def __init__(self, ilgis, plotis):
        self.ilgis = ilgis
        self.plotis = plotis

    def plotas(self): #tusti metodai, kadangi skaiciavimo formules skiriasi priklausomai nuo figuros
        pass

    def perimetras(self): #tusti metodai, kadangi skaiciavimo formules skiriasi priklausomai nuo figuros
        pass
class Stačiakampis(Figūra):
    def __init__(self, ilgis, plotis):
        super().__init__(ilgis, plotis)
    def plotas(self):
        return f'Stačiakampio plotas = {self.ilgis * self.plotis}'
    def perimetras(self):
        return f'Stačiakampio perimetras = {2 * (self.ilgis + self.plotis)}'

class StatusisTrikampis(Figūra):
    def __init__(self, statinis1, statinis2, izambine): #pasirinkau daryti ne su paveldejimu, kadangi staciajam trikampiui reikalingi kiti parametrai
        self.statinis1 = statinis1
        self.statinis2 = statinis2
        self.izambine = izambine

    def plotas(self):
        return f'Stačiojo trikampio plotas = {(self.statinis1 * self.statinis2)/2}'

    def perimetras(self):
        return f'Stačiojo trikampio perimetras = {self.statinis1 + self.statinis2 + self.izambine}'
staciakampis1 = Stačiakampis(3,5)
print(staciakampis1.plotas())
print(staciakampis1.perimetras())

trikampis1 = StatusisTrikampis(3,6,6.7)
print(trikampis1.plotas())
print(trikampis1.perimetras())