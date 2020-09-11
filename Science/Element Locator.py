__author__ = "Kevin"
__Liscence  = "Unliscenced"

import sys
from time import sleep
import webbrowser as wb

#exit protocol
def user_exit():
    user_exit = input("Quit (Y/N)")
    if user_exit == "Y":
        print("Goodbye")
        sys.exit(0)
    elif user_exit == "N":
        print("Returning to main menu...")
        sleep(0.5)
        return

#introduction
print("Hello, welcome to the Element Locator\n")
#main loop
while True:
    print(
        '''
        Press 1 to find an element by its symbol
        Press 2 to find a symbol by its element
        Press 3 to find an element by its atomic number
        '''
    )
    user_choice = int(input("Select an option: "))
    if user_choice == 1:

        user_element = input("Input the symbol of your element: ")

        def findElement(symbol):
            Elements = {
                #source = (https://en.wikipedia.org/wiki/List_of_chemical_elements)
                "H": "Hydrogen",
                "He": "Helium",
                "Li": "Lithium",
                "Be": "Beryllium",
                "B": "Boron",
                "C": "Carbon",
                "N": "Nitrogen",
                "O": "Oxygen",
                "F": "Fluorine",
                "Ne": "Neon",
                "Na": "Sodium",
                "Mg": "Magnesium",
                "Al": "Aluminium",
                "Si": "Silicon",
                "P": "Phosphours",
                "S": "Sulfur",
                "Cl": "Chlorine",
                "Ar": "Argon",
                "K": "Potassium",
                "Ca": "Calcium",
                "Sc": "Scandium",
                "Ti": "Titanium",
                "V": "Vanadium",
                "Cr": "Chromium",
                "Mn": "Manganese",
                "Fe": "Iron",
                "Co": "Colbolt",
                "Ni": "Nikel",
                "Cu": "Copper",
                "Zn": "Zinc",
                "Ga": "Gallium",
                "Ge": "Germanium",
                "As": "Arsenic",
                "Se": "Selenium",
                "Br": "Bromine",
                "Kr": "Krypton",
                "Rb": "Rubidium",
                "St": "Strontium",
                "Y": "Yittrium",
                "Zr": "Zinconium",
                "Nb": "Niobium",
                "Mo": "Molybdenum",
                "Tc": "Technetium",
                "Ru": "Ruthenium",
                "Rh": "Rhodium",
                "Pd": "Palladium",
                "Ag": "Silver",
                "Cd": "Cadmium",
                "In": "Indium",
                "Sn": "Tin",
                "Sb": "Anitmony",
                "Te": "Tellurium",
                "I": "Iodine",
                "Xe": "Xenon",
                "Cs": "Caesium",
                "Ba": "Barium",
                "La": "Lanthanum",
                "Ce": "Cerium",
                "Pr": "Praseodymium",
                "Nd": "Neodymium",
                "Pm": "Promethium",
                "Sm": "Samarium",
                "Eu": "Europium",
                "Gd": "Gadolinium",
                "Tb": "Terbium",
                "Dy": "Dysprosium",
                "Ho": "Holmium",
                "Er": "Erbium",
                "Tm": "Thulium",
                "Yb": "Yitterbium",
                "Lu": "Lutetium",
                "Hf": "Hafnium",
                "Ta": "Tantalum",
                "W": "Tungsten",
                "Re": "Rhenium",
                "Os": "Osmium",
                "Ir": "Iridium",
                "Pt": "Platinum",
                "Au": "Gold",
                "Hg": "Mercury",
                "Tl": "Thallium",
                "Pb": "Lead",
                "Bi": "Bismuth",
                "Po": "Polonium",
                "At": "Astatine",
                "Rn": "Radon",
                "Fr": "Francium",
                "Ra": "Radium",
                "Ac": "Actinium",
                "Th": "Thorium",
                "Pa": "Protactinium",
                "U": "Uranium",
                "Np": "Neptunium",
                "Pu": "Plutonium",
                "Am": "Americium",
                "Cm": "Curium",
                "Bk": "Berkelium",
                "Cf": "Californium",
                "Es": "Einsteinium",
                "Fm": "Fermium",
                "Md": "Mendelevium",
                "No": "Nobelium",
                "Lr": "Lawrencium",
                "Rf": "Rutherfordium",
                "Db": "Dubnium",
                "Sg": "Seaborgium",
                "Bh": "Bohrium",
                "Hs": "Hassium",
                "Mt": "Meitnerium",
                "Ds": "Darmstadtium",
                "Rg": "Roentgenium",
                "Cn": "Coppernicium",
                "Nh": "Nihonium",
                "Fl": "Flevorium",
                "Mc": "Moscovium",
                "Lv": "Livermorium",
                "Ts": "Tennessine",
                "Of": "Oganesson"
            }
            #for symbol in Elements.keys():
            if user_element in Elements:
                print(f"The element is:", Elements[user_element])
                user_exit()
            else:
                user_end = input(f"Looks like we didnt find {user_element} would you like google to be searched for an answer? (Y/N): ")
                if user_end == "Y":
                    print("Searching through Google...")
                    sleep(0.5)
                    wb.open('https://google.com/search?q='+user_element+'(element)', new=2)
                    user_exit()
                elif user_end == "N":
                    print("Roger that..")
                    user_exit()
        findElement(user_element)
    elif user_choice == 2:
        user_element = input("Input the name of your element: ")
        Elements = {
            #source = (https://en.wikipedia.org/wiki/List_of_chemical_elements)
            "H": "Hydrogen",
            "He": "Helium",
            "Li": "Lithium",
            "Be": "Beryllium",
            "B": "Boron",
            "C": "Carbon",
            "N": "Nitrogen",
            "O": "Oxygen",
            "F": "Fluorine",
            "Ne": "Neon",
            "Na": "Sodium",
            "Mg": "Magnesium",
            "Al": "Aluminium",
            "Si": "Silicon",
            "P": "Phosphours",
            "S": "Sulfur",
            "Cl": "Chlorine",
            "Ar": "Argon",
            "K": "Potassium",
            "Ca": "Calcium",
            "Sc": "Scandium",
            "Ti": "Titanium",
            "V": "Vanadium",
            "Cr": "Chromium",
            "Mn": "Manganese",
            "Fe": "Iron",
            "Co": "Colbolt",
            "Ni": "Nikel",
            "Cu": "Copper",
            "Zn": "Zinc",
            "Ga": "Gallium",
            "Ge": "Germanium",
            "As": "Arsenic",
            "Se": "Selenium",
            "Br": "Bromine",
            "Kr": "Krypton",
            "Rb": "Rubidium",
            "St": "Strontium",
            "Y": "Yittrium",
            "Zr": "Zinconium",
            "Nb": "Niobium",
            "Mo": "Molybdenum",
            "Tc": "Technetium",
            "Ru": "Ruthenium",
            "Rh": "Rhodium",
            "Pd": "Palladium",
            "Ag": "Silver",
            "Cd": "Cadmium",
            "In": "Indium",
            "Sn": "Tin",
            "Sb": "Anitmony",
            "Te": "Tellurium",
            "I": "Iodine",
            "Xe": "Xenon",
            "Cs": "Caesium",
            "Ba": "Barium",
            "La": "Lanthanum",
            "Ce": "Cerium",
            "Pr": "Praseodymium",
            "Nd": "Neodymium",
            "Pm": "Promethium",
            "Sm": "Samarium",
            "Eu": "Europium",
            "Gd": "Gadolinium",
            "Tb": "Terbium",
            "Dy": "Dysprosium",
            "Ho": "Holmium",
            "Er": "Erbium",
            "Tm": "Thulium",
            "Yb": "Yitterbium",
            "Lu": "Lutetium",
            "Hf": "Hafnium",
            "Ta": "Tantalum",
            "W": "Tungsten",
            "Re": "Rhenium",
            "Os": "Osmium",
            "Ir": "Iridium",
            "Pt": "Platinum",
            "Au": "Gold",
            "Hg": "Mercury",
            "Tl": "Thallium",
            "Pb": "Lead",
            "Bi": "Bismuth",
            "Po": "Polonium",
            "At": "Astatine",
            "Rn": "Radon",
            "Fr": "Francium",
            "Ra": "Radium",
            "Ac": "Actinium",
            "Th": "Thorium",
            "Pa": "Protactinium",
            "U": "Uranium",
            "Np": "Neptunium",
            "Pu": "Plutonium",
            "Am": "Americium",
            "Cm": "Curium",
            "Bk": "Berkelium",
            "Cf": "Californium",
            "Es": "Einsteinium",
            "Fm": "Fermium",
            "Md": "Mendelevium",
            "No": "Nobelium",
            "Lr": "Lawrencium",
            "Rf": "Rutherfordium",
            "Db": "Dubnium",
            "Sg": "Seaborgium",
            "Bh": "Bohrium",
            "Hs": "Hassium",
            "Mt": "Meitnerium",
            "Ds": "Darmstadtium",
            "Rg": "Roentgenium",
            "Cn": "Coppernicium",
            "Nh": "Nihonium",
            "Fl": "Flevorium",
            "Mc": "Moscovium",
            "Lv": "Livermorium",
            "Ts": "Tennessine",
            "Of": "Oganesson"
        }
        ElementsFlipped = {value:key for key, value in Elements.items()} #flipping the dictionary\
        def findElementByName(word):
            if user_element in ElementsFlipped.keys():
                print(f"The symbol is,", ElementsFlipped[user_element])
        findElementByName(user_element)
        user_exit()

    elif user_choice == 3:
        pass
    else:
        print("Invalid input...")
        sleep(0.5)
        print("Returning...")
        user_exit()