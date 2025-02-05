DictionarieOne = {
    'a': 1, 
    'b': 2
}
DictionarieTwo = {
    'c': 3,
    'd': 4
}

def Merge():
    DictionarieOne.update(DictionarieTwo)
    print(DictionarieOne)

Merge()