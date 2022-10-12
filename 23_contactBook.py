contactBook = {}

def addNewContact(name, number):
    contactBook[name]=number

def checkIfExist(name, number):
    contactExist = False
    if contactBook.get(name):
        if contactBook[name]==number:
            contactExist=True
    return contactExist

def checkContactBook():
    keepAdd = 'YES'
    while keepAdd=='YES' or keepAdd=='y':
        name = input("Enter the name: ")
        number = int(input("Enter phone number: "))
        if checkIfExist(name, number):
            print("The contact already exist")
        else:
            addNewContact(name, number)
        keepAdd = input("Keep adding?")
    
    print(contactBook)

checkContactBook()
