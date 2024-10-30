from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    def __init__(self, message):
        super().__init__(message)

def formel(queue):
    # <formel>::= <mol> \n
    # OBS EJ KLAR
    if mol(queue):
        return True
    return False

def mol(queue):
    # <mol>   ::= <group> | <group><mol>
    # OBS EJ KLAR
    if queue.isEmpty():
        raise Syntaxfel("Saknad stor bokstav vid radslutet.")
    
    if not group(queue):
        return False
    else: 
        if mol(queue):
            if not queue.isEmpty():
                if num(queue):
                    return True
                if queue.peek() == ")":
                    return True
                else:
                    raise Syntaxfel(f"Saknad högerparentes vid radslutet {queue.remainingQueue()}")
        return False
    

def group(queue):
    # <group> ::= <atom> |<atom><num> | (<mol>) <num>
    if atom(queue):
        if num(queue):
            return True
    if queue.peek() == "(":
        queue.dequeue()
        if mol(queue):
            print(queue.remainingQueue())
            if queue.peek() == ")":
                queue.dequeue()
                if num(queue):
                    return True
            raise Syntaxfel(f"Saknad högerparentes vid radslutet {queue.remainingQueue()}")
    raise Syntaxfel(f"Felaktig gruppstart vid radslutet {queue.remainingQueue()}")    

def atom(queue):
    # <atom>  ::= <LETTER> | <LETTER><letter>
    atoms = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv".split()

    letter1 = queue.peek()  # Titta på första tecknet
    myAtom = letter1
    if LETTER(letter1):
        queue.dequeue()  # Ta bort den första bokstaven
        if not queue.isEmpty() and letter(queue.peek()):
            letter2 = queue.dequeue()  # Ta bort den lilla bokstaven om den finns
            myAtom = letter1 + letter2
            for atom in atoms:  # Går igenom alla faktiska atomer för att kolla att det är en legit atom.
                if myAtom == atom:
                    return True
            raise Syntaxfel(f"Okänd atom vid radslutet {queue.remainingQueue()}")
        for atom in atoms:  # Går igenom alla faktiska atomer för att kolla att det är en legit atom.
            if myAtom == atom:
                return True # Ifall vi bara har en stor bokstav
        raise Syntaxfel(f"Okänd atom vid radslutet {queue.remainingQueue()}")
    else:
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {queue.remainingQueue()}")

def LETTER(char):
    # <LETTER>::= A | B | C | ... | Z
    return 'A' <= char <= 'Z'

def letter(char):
    # <letter>::= a | b | c | ... | z
    return 'a' <= char <= 'z'

def num(queue):
    # <num>   ::= 2 | 3 | 4 | ...
    numStr = ""
    hasDigits = False  # Flagga för att se om vi har hittat siffror

    while not queue.isEmpty() and queue.peek().isdigit():   # Kö är ej tom och nästkommande är en siffra
        numStr += queue.peek()  # Hämta tecknet utan att ta bort det
        hasDigits = True
        queue.dequeue() # Ta bort siffran

    if hasDigits:
        if numStr[0] == "0":  # Kontrollera om numStr börjar med 0
            remaining = numStr[1:]  # Ta reda på kvarvarande tecken
            raise Syntaxfel(f"För litet tal vid radslutet {remaining + queue.remainingQueue()}")
        if numStr[0] == "1":
            remaining = numStr[1:]
            if remaining == "":
                raise Syntaxfel(f"För litet tal vid radslutet {remaining + queue.remainingQueue()}")
            if queue().peek().isdigit():
                return True
            else:
                remaining = numStr[1:]  # Ta reda på kvarvarande tecken
                raise Syntaxfel(f"För litet tal vid radslutet {remaining + queue.remainingQueue()}")
        if int(numStr) >= 2:
            return True
    else: 
        return False

def main():    
    while True:
        molecule = input("")
        if molecule == "#":
            break
        
        # Skapa en kö av strängen
        queue = LinkedQ()
        for char in molecule:
            queue.enqueue(char)
        
        # Kontrollera om det är en korrekt molekyl
        try:
            if formel(queue):
                print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as e:
            print(e)  # Skriv bara ut felmeddelandet

main()