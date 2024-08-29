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

### TESTING

import unittest
from linkedQFile import LinkedQ

class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        #isEmpty ska returnera True för tom kö, False annars
        q = LinkedQ()
        self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
        q.enqueue(17)
        self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

    def test_order(self):
        #Kontrollerar att kö-ordningen blir rätt
        q = LinkedQ()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)

if __name__ == "__main__":
    unittest.main()