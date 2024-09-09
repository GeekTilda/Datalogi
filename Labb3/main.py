from bintreeFile import Bintree
import sys

def main():
    tree = Bintree()
    initializeTreeFromInput(tree)

def readInput():
    line = sys.stdin.readline().strip()
    numbers = line.split()
    return numbers

def initializeTreeFromInput(tree):    # Makes our treee :)
    numbers = readInput()
    for num in numbers:
        tree.put(int(num))

main()