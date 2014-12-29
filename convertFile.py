import argparse
Version = '0.1'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("convertFrom", help="File to convert.")
    parser.add_argument("convertTo",help="File to be written to.")
    parser.add_argument('-b','--toBinary',help="Convert to binary", action='store_true')
    parser.add_argument('-t','--toText',help="Convert to text",action='store_true')

    args = parser.parse_args()

    if args.toBinary:
        convert = toBin(args.convertFrom, args.convertTo)

    if args.toText:
        convert = toText(args.convertFrom, args.convertTo)

####################################################

class toBin:
    """Convert text to binary."""

    results = ""

    def __init__(self, fileIn, fileOut):
        self.fileIn = fileIn
        self.fileOut = fileOut
        self.forLoopOnText()
        

    def forLoopOnText(self):
        file = open(self.fileIn, 'r')
        for line in file:
            for letter in line:
                getOrd = ord(letter)
                toBin = bin(getOrd)
                self.results += toBin
                self.results += ' '
            self.results += '\n'
        file.close()
        #print(self.results)
        self.writeToFile()
        

    def writeToFile(self):
        with open(self.fileOut,'w') as file:
            file.write(self.results)

####################################################

class toText:
    """Convert binary to text."""

    tempList = []
    empty = ''
    results = ""

    def __init__(self, fileIn, fileOut):
        self.fileIn = fileIn
        self.fileOut = fileOut
        self.forLoopOnBinary()
        

    def forLoopOnBinary(self):
        file = open(self.fileIn, 'r')
        for line in file:
            for char in line:
                if char != ' ':
                    self.empty += char
                else:
                    self.tempList.append(self.empty)
                    self.empty = ''
        file.close()
        self.convertBin()

    def convertBin(self):
        for t in self.tempList:
            Num = int(t ,2)
            Char = chr(Num)
            self.results += Char
            #self.results += " "
        #print(self.results)
        self.writeToFile()

    
    def writeToFile(self):
        with open(self.fileOut,'w') as file:
            file.write(self.results)



if __name__ == '__main__':
    main()
