from linkedQFile import LinkedQ
from molgrafik import Molgrafik, Ruta

### DICTIONARY AV ATOMVIKTER FRÅN LABB 7
atomVikter = {
    "H": 1.00794,
    "He": 4.002602,
    "Li": 6.941,
    "Be": 9.012182,
    "B": 10.811,
    "C": 12.0107,
    "N": 14.0067,
    "O": 15.9994,
    "F": 18.9984032,
    "Ne": 20.1797,
    "Na": 22.98976928,
    "Mg": 24.3050,
    "Al": 26.9815386,
    "Si": 28.0855,
    "P": 30.973762,
    "S": 32.065,
    "Cl": 35.453,
    "K": 39.0983,
    "Ar": 39.948,
    "Ca": 40.078,
    "Sc": 44.955912,
    "Ti": 47.867,
    "V": 50.9415,
    "Cr": 51.9961,
    "Mn": 54.938045,
    "Fe": 55.845,
    "Ni": 58.6934,
    "Co": 58.933195,
    "Cu": 63.546,
    "Zn": 65.38,
    "Ga": 69.723,
    "Ge": 72.64,
    "As": 74.92160,
    "Se": 78.96,
    "Br": 79.904,
    "Kr": 83.798,
    "Rb": 85.4678,
    "Sr": 87.62,
    "Y": 88.90585,
    "Zr": 91.224,
    "Nb": 92.90638,
    "Mo": 95.96,
    "Tc": 98,
    "Ru": 101.07,
    "Rh": 102.90550,
    "Pd": 106.42,
    "Ag": 107.8682,
    "Cd": 112.411,
    "In": 114.818,
    "Sn": 118.710,
    "Sb": 121.760,
    "I": 126.90447,
    "Te": 127.60,
    "Xe": 131.293,
    "Cs": 132.9054519,
    "Ba": 137.327,
    "La": 138.90547,
    "Ce": 140.116,
    "Pr": 140.90765,
    "Nd": 144.242,
    "Pm": 145,
    "Sm": 150.36,
    "Eu": 151.964,
    "Gd": 157.25,
    "Tb": 158.92535,
    "Dy": 162.500,
    "Ho": 164.93032,
    "Er": 167.259,
    "Tm": 168.93421,
    "Yb": 173.054,
    "Lu": 174.9668,
    "Hf": 178.49,
    "Ta": 180.94788,
    "W": 183.84,
    "Re": 186.207,
    "Os": 190.23,
    "Ir": 192.217,
    "Pt": 195.084,
    "Au": 196.966569,
    "Hg": 200.59,
    "Tl": 204.3833,
    "Pb": 207.2,
    "Bi": 208.98040,
    "Po": 209,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226,
    "Ac": 227,
    "Th": 232.03806,
    "Pa": 231.03588,
    "U": 238.02891,
    "Np": 237,
    "Pu": 244,
    "Am": 243,
    "Cm": 247,
    "Bk": 247,
    "Cf": 251,
    "Es": 252,
    "Fm": 257,
    "Md": 258,
    "No": 259,
    "Lr": 262,
    "Rf": 265,
    "Db": 268,
    "Sg": 271,
    "Bh": 272,
    "Hs": 270,
    "Mt": 276,
    "Rg": 280,
    "Ds": 281,
    "Cn": 285
}

class Syntaxfel(Exception):
    pass

def formel(queue):
    # <formel> ::= <mol> \n
    tfm, first = mol(queue)
    # Kontrollera att det inte finns kvarvarande tecken efter formeln
    if not queue.isEmpty():
        raise Syntaxfel(f"Felaktig gruppstart vid radslutet {queue.remainingQueue()}")
    return True, first

def mol(queue):
    # <mol> ::= <group> | <group><mol> 
    first = None
    current = None
    # Kolla om fler grupper kan komma
    while not queue.isEmpty() and queue.peek() != ")":
        tfg, rutan = group(queue)
        if not tfg:  # Om nästa inte är en giltig grupp, avsluta
            return False, None
        if first is None:
            first = rutan
            current = rutan
        else:
            current.next = rutan
            current = rutan
    return True, first

def group(queue):
    rutan = Ruta()
    # <group> ::= <atom> |<atom><num> | (<mol>) <num>
    # Kontrollera om gruppen börjar med en parentes
    if queue.peek() == "(":
        queue.dequeue()  # Ta bort öppningsparentesen
        tfg, molruta = mol(queue)
        rutan.down = molruta
        if queue.peek() == ")":
            queue.dequeue()  # Ta bort slutparentesen
            if not num(queue, rutan):  # Kontrollera om det finns ett nummer
                raise Syntaxfel(f"Saknad siffra vid radslutet {queue.remainingQueue()}")
            return True, rutan
        raise Syntaxfel(f"Saknad högerparentes vid radslutet {queue.remainingQueue()}")

    # Kontrollera om queue är tom eller om det är en ogiltig karaktär
    if queue.isEmpty() or queue.peek() == ")":
        raise Syntaxfel(f"Felaktig gruppstart vid radslutet {queue.remainingQueue()}")

    # Kontrollera om tecknet är en siffra
    if queue.peek().isdigit():
        raise Syntaxfel(f"Felaktig gruppstart vid radslutet {queue.remainingQueue()}")

    elif atom(queue, rutan):  # Annars ska gruppen börja med en atom
        num(queue, rutan)  # Kontrollera om ett valfritt nummer finns
        return True, rutan

    raise Syntaxfel(f"Felaktig gruppstart vid radslutet {queue.remainingQueue()}")


def atom(queue, rutan):
    # <atom>  ::= <LETTER> | <LETTER><letter>
    atoms = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv".split()

    if not LETTER(queue.peek()):
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {queue.remainingQueue()}")
    
    myAtom = queue.dequeue()
    if not queue.isEmpty() and letter(queue.peek()):
        myAtom += queue.dequeue()
    
    if myAtom not in atoms:
        raise Syntaxfel(f"Okänd atom vid radslutet {queue.remainingQueue()}")
    
    rutan.atom = myAtom
    return True

def LETTER(char):
    # <LETTER>::= A | B | C | ... | Z
    return 'A' <= char <= 'Z'

def letter(char):
    # <letter>::= a | b | c | ... | z
    return 'a' <= char <= 'z'

def num(queue, rutan):
    # <num>   ::= 2 | 3 | 4 | ...
    numStr = ""
    while not queue.isEmpty() and queue.peek().isdigit():
        numStr += queue.dequeue()

    if numStr:
        if numStr[0] == "0" or numStr == "1":
            raise Syntaxfel(f"För litet tal vid radslutet {numStr[1:] + queue.remainingQueue()}")
        else:
            rutan.num = int(numStr)
            return True
    return False

def weight(rutan):
    vikt = 0
    if rutan.atom == "()":
        viktPar = weight(rutan.down) * (rutan.num - 1)
        vikt = vikt + viktPar
    else:
        vikt = atomVikter.get(rutan.atom) * rutan.num

    if rutan.down == None:
        if rutan.next == None:
            return vikt
        else:
            return vikt + weight(rutan.next)
    else:
        return vikt + weight(rutan.down)


def main():    
    while True:
        molecule = input("")
        if molecule == "#":
            break
        
        queue = LinkedQ()
        for char in molecule:
            queue.enqueue(char)
        
        try:
            synKorr, first = formel(queue)
            if synKorr:
                print("Formeln är syntaktiskt korrekt")
                print(weight(first))
                mg = Molgrafik()
                mg.show(first)
        except Syntaxfel as e:
            print(e)

main()