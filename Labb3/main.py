from bintreeFile import Bintree

def makeTree():
    tree = Bintree()
    data = input().strip()
    while data != "#":
        tree.put(data)
        data = input().strip()
    return tree

def searches(tree):
    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()

def main():
    tree = makeTree()
    searches(tree)

main()