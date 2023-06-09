import logging
logging.basicConfig(filename='log.txt', level=logging.INFO)

ilgis = float(input("Ilgis: "))
plotis = float(input("Plotis: "))
def staciakampio_plotas_perimetras():
    plotas = ilgis * plotis
    perimetras = 2 * (ilgis+plotis)
    rezultatas =f'Plotas = {plotas} cm; perimetras = {perimetras} cm.'
    logging.info(rezultatas)
    return rezultatas

print(staciakampio_plotas_perimetras())
