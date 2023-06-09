from PIL import Image, ImageEnhance

def nustatyti_kontrasta():
    pavadinimas = input("Nurodykite paveiksliuko pavadinimą: ")
    image = Image.open(pavadinimas)
    image.show()
    kontrastas = int(input("Nustatykite kontrasta: "))
    enh = ImageEnhance.Contrast(image)
    image = enh.enhance(kontrastas)
    image.show()
    print("Ar išsaugoti? Y/N?")
    save = input("Įveskite: ")
    if save == "Y":
        name = input("Iveskite pavadinimą ir formatą: ")
        image.save(name)
        print(f"Paveiksliukas išsaugotas pavadinimu {name}")
    else:
        print("Paveiksliukas neišsaugotas")

nustatyti_kontrasta()