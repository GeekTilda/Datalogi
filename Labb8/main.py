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
        # Använd hela kön efter felet
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {queue.remainingQueue()}")

def LETTER(char):
    return 'A' <= char <= 'Z'

def letter(char):
    return 'a' <= char <= 'z'

def num(queue):
    numStr = ""
    while not queue.isEmpty() and queue.peek().isdigit():
        numStr += queue.dequeue()

    if numStr and int(numStr) >= 2:
        return True
    else:
        # Använd hela kön efter felet
        raise Syntaxfel(f"För litet tal vid radslutet {queue.remainingQueue()}")

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
            print(f"{e}")

main()
