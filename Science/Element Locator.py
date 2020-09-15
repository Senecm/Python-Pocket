__author__ = "Kevin"
__Liscence  = "Unliscenced"

from time import sleep
import webbrowser as wb

#exit protocol
def user_exit():
    user_exit = input("Quit (Y/N)")
    if user_exit == "Y":
        print("Goodbye")
        quit(0)
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
        Press 4 to find an atomic number by its element
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
            "Og": "Oganesson"
        }
        ElementsFlipped = {value:key for key, value in Elements.items()} #flipping the dictionary\
        def findElementByName(word):
            if user_element in ElementsFlipped.keys():
                print(f"The symbol is,", ElementsFlipped[user_element])
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
        findElementByName(user_element)
        #calling the exit function
        user_exit()
    elif user_choice == 3:
        user_element = input("Enter the atomic number of your element: ")
        Elements = {
            #source = (https://en.wikipedia.org/wiki/List_of_chemical_elements)
            "1": "Hydrogen",
            "2": "Helium",
            "3": "Lithium",
            "4": "Beryllium",
            "5": "Boron",
            "6": "Carbon",
            "7": "Nitrogen",
            "8": "Oxygen",
            "9": "Fluorine",
            "10": "Neon",
            "11": "Sodium",
            "12": "Magnesium",
            "13": "Aluminium",
            "14": "Silicon",
            "15": "Phosphours",
            "16": "Sulfur",
            "17": "Chlorine",
            "18": "Argon",
            "19": "Potassium",
            "20": "Calcium",
            "21": "Scandium",
            "22": "Titanium",
            "23": "Vanadium",
            "24": "Chromium",
            "25": "Manganese",
            "26": "Iron",
            "27": "Colbolt",
            "28": "Nikel",
            "29": "Copper",
            "30": "Zinc",
            "31": "Gallium",
            "32": "Germanium",
            "33": "Arsenic",
            "34": "Selenium",
            "35": "Bromine",
            "36": "Krypton",
            "37": "Rubidium",
            "38": "Strontium",
            "39": "Yittrium",
            "40": "Zinconium",
            "41": "Niobium",
            "42": "Molybdenum",
            "43": "Technetium",
            "44": "Ruthenium",
            "45": "Rhodium",
            "46": "Palladium",
            "47": "Silver",
            "48": "Cadmium",
            "49": "Indium",
            "50": "Tin",
            "51": "Anitmony",
            "52": "Tellurium",
            "53": "Iodine",
            "54": "Xenon",
            "55": "Caesium",
            "56": "Barium",
            "57": "Lanthanum",
            "58": "Cerium",
            "59": "Praseodymium",
            "60": "Neodymium",
            "61": "Promethium",
            "62": "Samarium",
            "63": "Europium",
            "64": "Gadolinium",
            "65": "Terbium",
            "66": "Dysprosium",
            "67": "Holmium",
            "68": "Erbium",
            "69": "Thulium",
            "70": "Yitterbium",
            "71": "Lutetium",
            "72": "Hafnium",
            "73": "Tantalum",
            "74": "Tungsten",
            "75": "Rhenium",
            "76": "Osmium",
            "77": "Iridium",
            "78": "Platinum",
            "79": "Gold",
            "80": "Mercury",
            "81": "Thallium",
            "82": "Lead",
            "83": "Bismuth",
            "84": "Polonium",
            "85": "Astatine",
            "86": "Radon",
            "87": "Francium",
            "88": "Radium",
            "89": "Actinium",
            "90": "Thorium",
            "91": "Protactinium",
            "92": "Uranium",
            "93": "Neptunium",
            "94": "Plutonium",
            "95": "Americium",
            "96": "Curium",
            "97": "Berkelium",
            "98": "Californium",
            "99": "Einsteinium",
            "100": "Fermium",
            "101": "Mendelevium",
            "102": "Nobelium",
            "103": "Lawrencium",
            "104": "Rutherfordium",
            "105": "Dubnium",
            "106": "Seaborgium",
            "107": "Bohrium",
            "108": "Hassium",
            "109": "Meitnerium",
            "110": "Darmstadtium",
            "111": "Roentgenium",
            "112": "Coppernicium",
            "113": "Nihonium",
            "114": "Flevorium",
            "115": "Moscovium",
            "116": "Livermorium",
            "117": "Tennessine",
            "118": "Oganesson"
        }
        if user_element in Elements.keys():
            print(f"The element is:", Elements[user_element])
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
        #calling the exit function
        user_exit()
    elif user_choice == 4:
        user_element = input("Enter the name of your element: ")
        Elements = {
            #source = (https://en.wikipedia.org/wiki/List_of_chemical_elements)
            "1": "Hydrogen",
            "2": "Helium",
            "3": "Lithium",
            "4": "Beryllium",
            "5": "Boron",
            "6": "Carbon",
            "7": "Nitrogen",
            "8": "Oxygen",
            "9": "Fluorine",
            "10": "Neon",
            "11": "Sodium",
            "12": "Magnesium",
            "13": "Aluminium",
            "14": "Silicon",
            "15": "Phosphours",
            "16": "Sulfur",
            "17": "Chlorine",
            "18": "Argon",
            "19": "Potassium",
            "20": "Calcium",
            "21": "Scandium",
            "22": "Titanium",
            "23": "Vanadium",
            "24": "Chromium",
            "25": "Manganese",
            "26": "Iron",
            "27": "Colbolt",
            "28": "Nikel",
            "29": "Copper",
            "30": "Zinc",
            "31": "Gallium",
            "32": "Germanium",
            "33": "Arsenic",
            "34": "Selenium",
            "35": "Bromine",
            "36": "Krypton",
            "37": "Rubidium",
            "38": "Strontium",
            "39": "Yittrium",
            "40": "Zinconium",
            "41": "Niobium",
            "42": "Molybdenum",
            "43": "Technetium",
            "44": "Ruthenium",
            "45": "Rhodium",
            "46": "Palladium",
            "47": "Silver",
            "48": "Cadmium",
            "49": "Indium",
            "50": "Tin",
            "51": "Anitmony",
            "52": "Tellurium",
            "53": "Iodine",
            "54": "Xenon",
            "55": "Caesium",
            "56": "Barium",
            "57": "Lanthanum",
            "58": "Cerium",
            "59": "Praseodymium",
            "60": "Neodymium",
            "61": "Promethium",
            "62": "Samarium",
            "63": "Europium",
            "64": "Gadolinium",
            "65": "Terbium",
            "66": "Dysprosium",
            "67": "Holmium",
            "68": "Erbium",
            "69": "Thulium",
            "70": "Yitterbium",
            "71": "Lutetium",
            "72": "Hafnium",
            "73": "Tantalum",
            "74": "Tungsten",
            "75": "Rhenium",
            "76": "Osmium",
            "77": "Iridium",
            "78": "Platinum",
            "79": "Gold",
            "80": "Mercury",
            "81": "Thallium",
            "82": "Lead",
            "83": "Bismuth",
            "84": "Polonium",
            "85": "Astatine",
            "86": "Radon",
            "87": "Francium",
            "88": "Radium",
            "89": "Actinium",
            "90": "Thorium",
            "91": "Protactinium",
            "92": "Uranium",
            "93": "Neptunium",
            "94": "Plutonium",
            "95": "Americium",
            "96": "Curium",
            "97": "Berkelium",
            "98": "Californium",
            "99": "Einsteinium",
            "100": "Fermium",
            "101": "Mendelevium",
            "102": "Nobelium",
            "103": "Lawrencium",
            "104": "Rutherfordium",
            "105": "Dubnium",
            "106": "Seaborgium",
            "107": "Bohrium",
            "108": "Hassium",
            "109": "Meitnerium",
            "110": "Darmstadtium",
            "111": "Roentgenium",
            "112": "Coppernicium",
            "113": "Nihonium",
            "114": "Flevorium",
            "115": "Moscovium",
            "116": "Livermorium",
            "117": "Tennessine",
            "118": "Oganesson"
        }
        ElementsFlipped = {value:key for key, value in Elements.items()} #flipping the dictionary\
        def findElementByName(word):
            if user_element in ElementsFlipped.keys():
                print(f"The atomic number is,", ElementsFlipped[user_element])
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
        findElementByName(user_element)
        #calling the exit function
        user_exit()

    else:
        print("Invalid input...")
        sleep(0.5)
        print("Returning...")
        #calling the exit function
        user_exit()