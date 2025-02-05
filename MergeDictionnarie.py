DictionarieOne = {
    'a': 1, 
    'd': 4
}
DictionarieTwo = {
    'c': 3,
    'd': 4
}

def Merge():
    DictionarieOne.update(DictionarieTwo)
    print(DictionarieOne)

def Common():
    print(DictionarieOne.keys() & DictionarieTwo.keys())
Common()