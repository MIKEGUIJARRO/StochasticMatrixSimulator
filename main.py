from util.Groups import Groups
from util.file import writeNewLine, cleanOutput

def runHandler():
    # Requests number of groups
    n = initialInput()

    # Generates the groups of warriors
    groups = Groups(n)
    cleanOutput()
    while(not groups.isScalar()):
        print(groups.matrix)
        print()
        print(groups.group)
        print()
        # Selects a random group to atack
        groups.groupRandomAtack()
        print()
        print(groups.group)
        print('\n\n--------------------------------\n\n')

        writeNewLine(groups.matrix)

        writeNewLine(groups.group)        
        # Selects a random group to atack
        groups.groupRandomAtack()
        writeNewLine(groups.group)
        writeNewLine('\n\n--------------------------------\n\n')

    print(groups.group)
    writeNewLine('Winner:')
    writeNewLine(groups.group)

def initialInput():
    userInput = ''
    while userInput is not int:
        try:
            userInput = input('Type the number of groups in this BRAWL!: ')
            break
        except:
            print('Please enter a valid number:')
    return int(userInput)


runHandler()
