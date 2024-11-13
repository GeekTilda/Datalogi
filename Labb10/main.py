from linkedQFile import LinkedQ
from molgrafik import Molgrafik, Ruta

### DICTIONARY OF ATOM WEIGTHS
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

def readFormula(q):
    # <formel> ::= <mol> \n
    tfm, first = readMol(q)
    # Checks for leftover symbols after the molecule.
    if not q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart")
    return True, first

def readMol(q):
    # <mol> ::= <group> | <group><mol> 
    first = None
    current = None
    
    while not q.isEmpty() and q.peek() != ")":
        tfg, rutan = readGroup(q)
        if not tfg:  # Break if next group is invalid.
            return False, None
        if first is None:
            first = rutan
            current = rutan
        else:
            current.next = rutan
            current = rutan
    return True, first

def readGroup(q):
    rutan = Ruta()
    # <group> ::= <atom> |<atom><num> | (<mol>) <num>
    # Check if the group starts with a parenthesis.
    if q.peek() == "(":
        q.dequeue()  # Remove "("
        _, molruta = readMol(q)
        rutan.down = molruta
        if q.peek() == ")":
            q.dequeue()  # Remove ")"
            if not readNum(q, rutan):  # Checks for numbers.
                raise Syntaxfel("Saknad siffra")
            return True, rutan
        raise Syntaxfel("Saknad högerparentes")

    # Checks if the queue is empty or if the next symbol is invalid.
    if q.isEmpty() or q.peek() == ")":
        raise Syntaxfel("Felaktig gruppstart")

    # Checks if the next symbol is a number.
    if q.peek().isdigit():
        raise Syntaxfel("Felaktig gruppstart")

    elif readAtom(q, rutan):  # Otherwise, the group starts with an atom.
        readNum(q, rutan)  # Checks for numbers.
        return True, rutan

    raise Syntaxfel("Felaktig gruppstart")


def readAtom(q, rutan):
    # <atom> ::= <LETTER> | <LETTER><letter>
    atoms = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv".split()

    if not readLETTER(q.peek()):
        raise Syntaxfel("Saknad stor bokstav")
    
    myAtom = q.dequeue()
    if not q.isEmpty() and readletter(q.peek()):
        myAtom += q.dequeue()
    
    if myAtom not in atoms:
        raise Syntaxfel("Okänd atom")
    
    rutan.atom = myAtom
    return True

def readLETTER(char):
    # <LETTER> ::= A | B | C | ... | Z
    return 'A' <= char <= 'Z'

def readletter(char):
    # <letter> ::= a | b | c | ... | z
    return 'a' <= char <= 'z'

def readNum(q, rutan):
    # <num> ::= 2 | 3 | 4 | ...
    numStr = ""
    while not q.isEmpty() and q.peek().isdigit():
        numStr += q.dequeue()

    if numStr:
        if numStr[0] == "0" or numStr == "1":
            raise Syntaxfel("För litet tal")
        else:
            rutan.num = int(numStr)
            return True
    return False

def weight(rutan):
    vikt = 0

    if rutan.atom == "()":
        viktPar = 0
        currentRuta = rutan.down

        # Loops through every atom in ()-group and adds its weight to total sum.
        while currentRuta != None:
            if currentRuta.atom == "()":
                viktPar += weight(currentRuta)
            else:
                viktPar += atomVikter.get(currentRuta.atom) * currentRuta.num
            currentRuta = currentRuta.next
        vikt = viktPar * rutan.num
    else:
        vikt = atomVikter.get(rutan.atom) * rutan.num
    
    if rutan.next == None:
        return vikt
    else:
        return vikt + weight(rutan.next)

def main():
    while True:
        mol = input()
        if mol == "#":
            break
        q = LinkedQ()
        for tkn in mol:
            q.enqueue(tkn)
        try:
            synCorr, first = readFormula(q)
            if synCorr:
                print("Formeln är syntaktiskt korrekt")
                print(weight(first))
                mg = Molgrafik()
                mg.show(first)
        except Syntaxfel as felet:
            rest = str(q).strip()
            print(felet, "vid radslutet", rest)

main()