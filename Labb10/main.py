from linkedQFile import LinkedQ
from molgrafik import Molgrafik, 

class Syntaxfel(Exception):
    pass

def formel(queue):
    # <formel> ::= <mol> \n
    tfm, first = mol(queue)
    # Kontrollera att det inte finns kvarvarande tecken efter formeln
    if not queue.isEmpty():
        raise Syntaxfel(f"Felaktig gruppstart vid radslutet {queue.remainingQueue()}")
    return True

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

def num(queue):
    # <num>   ::= 2 | 3 | 4 | ...
    numStr = ""
    while not queue.isEmpty() and queue.peek().isdigit():
        numStr += queue.dequeue()

    if numStr:
        if numStr[0] == "0" or numStr == "1":
            raise Syntaxfel(f"För litet tal vid radslutet {numStr[1:] + queue.remainingQueue()}")
        else:
            rutan.num = numStr
            return True
    return False

def main():    
    while True:
        molecule = input("")
        if molecule == "#":
            break
        
        queue = LinkedQ()
        for char in molecule:
            queue.enqueue(char)
        
        try:
            if formel(queue):
                print("Formeln är syntaktiskt korrekt")
                mg = molgrafik.Molgrafik()
                mg.show(molecule)
        except Syntaxfel as e:
            print(e)

main()