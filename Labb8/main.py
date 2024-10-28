from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    def __init__(self, message):
        super().__init__(message)

def molekyl(queue):
    if queue.isEmpty():
        raise Syntaxfel("Saknad stor bokstav vid radslutet.")
    
    if atom(queue):
        if not queue.isEmpty():
            if num(queue):
                return True
            else:
                return False
        return True  # Molekyl som bara är en atom
    return False

def atom(queue):
    letter1 = queue.peek()  # Titta på första tecknet
    if LETTER(letter1):
        queue.dequeue()  # Ta bort den första bokstaven
        if not queue.isEmpty() and letter(queue.peek()):
            queue.dequeue()  # Ta bort den lilla bokstaven om den finns
        return True
    else:
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {queue.remainingQueue()}")

def LETTER(char):
    return 'A' <= char <= 'Z'

def letter(char):
    return 'a' <= char <= 'z'

def num(queue):
    numStr = ""
    hasDigits = False  # Flagga för att se om vi har hittat siffror

    while not queue.isEmpty() and queue.peek().isdigit():
        numStr += queue.peek()  # Hämta tecknet utan att ta bort det
        hasDigits = True
        queue.dequeue()

    if hasDigits:
        if numStr[0] == "0":  # Kontrollera om numStr börjar med 0
            remaining = numStr[1:]  # Ta reda på kvarvarande tecken
            raise Syntaxfel(f"För litet tal vid radslutet {remaining}")

        if int(numStr) >= 2:
            return True

    remaining = queue.remainingQueue()
    raise Syntaxfel(f"För litet tal vid radslutet {remaining}")

def main():    
    while True:
        atom = input("")
        if atom == "#":
            break
        
        # Skapa en kö av strängen
        queue = LinkedQ()
        for char in atom:
            queue.enqueue(char)
        
        # Kontrollera om det är en korrekt molekyl
        try:
            if molekyl(queue):
                print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as e:
            print(e)  # Skriv bara ut felmeddelandet

main()
