from arrayQFile import ArrayQ

### MAIN
        
def main():
    queue = ArrayQ()
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

### CALLING MAIN

main()