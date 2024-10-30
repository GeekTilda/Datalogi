from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    def __init__(self, message):
        super().__init__(message)

def formel(queue):
    mol(queue)
    # Kontrollera att det inte finns kvarvarande tecken efter formeln
    if not queue.isEmpty():
        raise Syntaxfel(f"Felaktig gruppstart vid radslutet {queue.remainingQueue()}")
    return True

def mol(queue):
    if not group(queue):  # Kontrollera första gruppen
        return False
    # Kolla om fler grupper kan komma
    while not queue.isEmpty() and queue.peek() not in ")":
        if not group(queue):  # Om nästa inte är en giltig grupp, avsluta
            return False
    return True

def group(queue):
    # Kontrollera om gruppen börjar med en parentes
    if queue.peek() == "(":
        queue.dequeue()  # Ta bort öppningsparentesen
        mol(queue)       # Hantera allt inom parenteserna
        if queue.peek() == ")":
            queue.dequeue()  # Ta bort slutparentesen
            num(queue)       # Kontrollera efterföljande nummer
            return True
        else:
            raise Syntaxfel(f"Saknad högerparentes vid radslutet {queue.remainingQueue()}")
    elif atom(queue):  # Annars ska gruppen börja med en atom
        num(queue)  # Kontrollera om ett valfritt nummer finns
        return True
    else:
        raise Syntaxfel(f"Felaktig gruppstart vid radslutet {queue.remainingQueue()}")

def atom(queue):
    atoms = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv".split()

    if not LETTER(queue.peek()):
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {queue.remainingQueue()}")
    
    myAtom = queue.dequeue()
    if not queue.isEmpty() and letter(queue.peek()):
        myAtom += queue.dequeue()
    
    if myAtom not in atoms:
        raise Syntaxfel(f"Okänd atom vid radslutet {queue.remainingQueue()}")
    return True

def LETTER(char):
    return 'A' <= char <= 'Z'

def letter(char):
    return 'a' <= char <= 'z'

def num(queue):
    numStr = ""
    while not queue.isEmpty() and queue.peek().isdigit():
        numStr += queue.dequeue()

    if numStr:
        if numStr[0] == "0" or numStr == "1":
            raise Syntaxfel(f"För litet tal vid radslutet {numStr[1:] + queue.remainingQueue()}")
        if int(numStr) >= 2:
            return True
    return False  # Inga siffror betyder att `num` är valfri och kan saknas


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
        except Syntaxfel as e:
            print(e)

main()
