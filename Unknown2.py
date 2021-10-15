print('''                       Now we are going onto dictionaries.
=================================================================================================================''')
myName = {'first name': 'john', 'last name': 'doe', 'age': 23}
print(''' =======================================================================================================''')
print(myName)
def dictionaryAnswer():
    for i in reversed(range(2)):
        userkeyAnswer = input('Is last name a key or a value?')
        print(f"You have {i} guesses left!")
        x = myName.get("last name")
    if userkeyAnswer != 'key':
        return "Incorrect! Try Again!"
    else:
        return 'Correct! It is {x}'

        

print(dictionaryAnswer())