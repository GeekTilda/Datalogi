def myHashFunction(word):
    output = ""

    for letter in word:
        value = str(ord(letter))
        output += value

    print(output)

inputWord = input("Vilket ord vill du hasha? ").upper()
myHashFunction(inputWord)