from linkedQFile import LinkedQ
import sys

### MAIN
        
def main():
    queue = LinkedQ()
    initializeQueueFromInput(queue)
    print("Storleken av vår kö: " + str(queue.size()))
    CardTrick(queue)
        
### FUNCTIONS 

def CardTrick(queue):
    printStr = ""
    while not (queue.isEmpty()):
        temp = queue.dequeue()
        if queue.isEmpty():
            printStr += temp
        else:
            printStr += str(queue.getFirst()) + " "
            queue.enqueue(temp)
            queue.dequeue()
    print(printStr)

def readInput():
    line = sys.stdin.readline().strip()
    numbers = line.split()
    return numbers

def initializeQueueFromInput(queue):    # Makes our queue :)
    numbers = readInput()
    for num in numbers:
        queue.enqueue(num)

### CALLING MAIN

main()

### 7 1 12 2 8 3 11 4 9 5 13 6 10