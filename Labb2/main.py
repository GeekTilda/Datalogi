from linkedQFile import LinkedQ
from linkedQFile import Node

### MAIN
        
def main():
    queue = LinkedQ()
    initializeQueue(queue, [7,1,12,2,8,3,11,4,9,5,13,6,10])
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

def initializeQueue(queue, values):
    for value in values:
        queue.enqueue(value)

### CALLING MAIN

main()