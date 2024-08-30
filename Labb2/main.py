from linkedQFile import LinkedQ
import sys

### MAIN
        
def main():
    queue = LinkedQ()
    initializeQueueFromInput(queue)
    CardTrick(queue)
        
### FUNCTIONS 

def CardTrick(queue):
    while not (queue.isEmpty()):
        temp = queue.dequeue()
        if queue.isEmpty():
            print(temp)
        else:
            print(queue)
            queue.enqueue(temp)
            queue.dequeue()

def readInput():
    line = sys.stdin.readline().strip()
    numbers = line.split()
    return [num for num in numbers]

def initializeQueueFromInput(queue):
    numbers = readInput()
    for num in numbers:
        queue.enqueue(num)

### CALLING MAIN

main()

### 7 1 12 2 8 3 11 4 9 5 13 6 10   