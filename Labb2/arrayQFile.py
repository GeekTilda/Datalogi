from array import array

class ArrayQ():
    
    def __init__(self):
        self._queue = [7,1,12,2,8,3,11,4,9,5,13,6,10]

    def __str__(self):  # Writes out the first element in queue
        return str(self._queue[0])

    def enqueue(self,n):    # Puts something last in our queue
        self._queue.append(n)

    def dequeue(self):  # Takes the first element of the queue out of it
        return self._queue.pop(0)
    
    def isEmpty(self):
        if self._queue.__len__() == 0:
            return True
        else:
            return False
