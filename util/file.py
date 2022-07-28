def writeNewLine(data):
    fileName = 'output.txt'
    f = open('data/' + fileName, 'a')
    f.write('\n' + str(data))
def cleanOutput():
    fileName = 'output.txt'
    f = open('data/' + fileName, 'w').close()