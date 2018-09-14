import random

class plugBoard:

     def __init__(self):
          self.connections = []

     #Add cable/wire to the plugboard
     def addWire(self, letterA, letterB):
     
          #Convert letterA to char
          letterA = ord(letterA)
          if letterA > 96:
               letterA -= 97
          else:
               letterA -= 65
               
          #Convert letterA to char
          letterB = ord(letterB)
          if letterB > 96:
               letterB -= 97
          else:
               letterB -= 65
     
          self.connections.append([letterA, letterB])
          
     #Get letter on other side of the cable
     def getLetter(self, charLetter):
          #Loop through every connection to find matching letter
          for i in self.connections:
               if i[0] == charLetter:
                    return i[1]
               elif i[1] == charLetter:
                    return i[0]
                    
          #If no letter found, return inputLetter
          return charLetter;
          
class reflectorWheel:
    
     def __init__(self, settings = ""):
     
          self.rotorWires = []
          self.numOfSymbols = 26
          
          if settings == "":
               self.scrambleConnections()
          else:
               self.readSettings(settings)
               
     #Scramble connection
     def scrambleConnections(self):
          '''for i in range(self.numOfSymbols):
               foundUnique = 0
               while not foundUnique:
                    foundUnique = 1
                    randomMatch = random.randint(0, self.numOfSymbols)
                    for wire in self.rotorWires:
                         if wire[0] == randomMatch:
                              foundUnique = 0
               self.rotorWires.append([i, randomMatch])
               self.rotorWires.append([randomMatch, i])'''
               
     #Reads in a settings string
     def readSettings(self, settingsStr):
          
          pos = 0;
          for c in settingsStr:
               symbolValue = ord(c)
               if symbolValue > 96:
                    symbolValue -= 97
               else:
                    symbolValue -= 65
               self.rotorWires.append(symbolValue)
               pos += 1
               
     #Get position on other side
     def getConnection(self, symbolNumber):
          return self.rotorWires[symbolNumber]
          
class rotorWheel:
    
     def __init__(self, settings = "", turnOverSymbol = "a"):
          self.rotorWires = []
          self.numOfSymbols = 26
          self.turnOverSymbol = turnOverSymbol
          
          if settings == "":
               self.scrambleConnections()
          else:
               self.readSettings(settings)
               
     #Reads in a settings string
     def readSettings(self, settingsStr):
          
          pos = 0;
          for c in settingsStr:
               symbolValue = ord(c)
               if symbolValue > 96:
                    symbolValue -= 97
               else:
                    symbolValue -= 65
               self.rotorWires.append(symbolValue)
               pos += 1
             
     #Scramble connection
     def scrambleConnections(self):
          for i in range(self.numOfSymbols):
               foundUnique = 0
               while not foundUnique:
                    foundUnique = 1
                    randomMatch = random.randint(0, self.numOfSymbols)
                    for wire in self.rotorWires:
                         if wire == randomMatch:
                              foundUnique = 0
               self.rotorWires.append(randomMatch)
               
     #Rotate list
     def rotate(self):
          self.rotorWires = [self.rotorWires[-1]] + self.rotorWires[:-1]
          
     #Get position on other side, 0 left direction 1 right direction
     def getConnection(self, symbolNumber, direction):
          if direction == 1:
               return self.rotorWires[symbolNumber]
          else:
               pos = 0
               for wire in self.rotorWires:
                    if wire == symbolNumber:
                         return pos
                    pos += 1     
          
class rotorColumn:
     
     def __init__(self):
          self.rotorWheels = []
          self.enteredLetters = 0
          
     def sendThroughSymbol(self, symbolValue, direction):
          currentValue = symbolValue
          if direction == 1:
               for rotorWheel in self.rotorWheels:
                    currentValue = rotorWheel.getConnection(currentValue, direction)
          else:
               for rotorWheel in reversed(self.rotorWheels):
                    currentValue = rotorWheel.getConnection(currentValue, 0)
          return currentValue
          
     #Rotate mechanism
     def turnOver(self):
     
          #Rotate first wheel, rightMost
          self.rotorWheels[0].rotate()
          
          currentPos = 0
          #Turn first wheel and check if any reaches turnOverSymbol
          for rotorWheel in self.rotorWheels:
               #If the wheel reached turnOverSymbol, rotate wheel to right
               if rotorWheel.rotorWires[0] == rotorWheel.turnOverSymbol:
                    #If rotorWheel exists on the left
                    if currentPos < len(self.rotorWheels):
                         self.rotorWheels[currentPos + 1].rotate()
               currentPos += 1
                             
     #Add rotorWheel to column
     def addWheel(self, rotorWheel):
          self.rotorWheels.append(rotorWheel)   
          
class enigmaMachine:

     def __init__(self):
          
          self.rotorColumn = rotorColumn()   
          self.plugBoard = plugBoard()
          self.reflector = None
          
     def encryptStr(self, message):
          encryptedMessage = ""
          for c in message:
               symbolValue = ord(c) - 97
               newSymbol = self.getSymbol(symbolValue)
               character = chr(newSymbol + 97)
               encryptedMessage += character
          return encryptedMessage
          
     def decryptStr(self, message):
          decryptedMessage = ""
          for c in message:
               symbolValue = ord(c) - 97
               newSymbol = self.getSymbol(symbolValue)
               character = chr(newSymbol + 97)
               decryptedMessage += character
          return decryptedMessage  
          
     #Send through letter
     def getSymbol(self, symbolVal):
          
          #Through plugboard
          nextSymbol = self.plugBoard.getLetter(symbolVal)
          
          #Through rotorColumn
          nextSymbol = self.rotorColumn.sendThroughSymbol(symbolVal, 1)
          
          #Through reflector
          nextSymbol = self.reflector.getConnection(nextSymbol)
          
          #Back through rotorColumn
          nextSymbol = self.rotorColumn.sendThroughSymbol(nextSymbol, 0)
          
          #Back through plugboard
          nextSymbol = self.plugBoard.getLetter(nextSymbol)
          
          #Rotate wheels
          self.rotorColumn.turnOver()
          
          return nextSymbol
          
     #Add rotorWheel to column
     def plugBoardAdd(self, letterA, letterB):
          self.plugBoard.addWire(letterA, letterB)   
          
     #Add rotorWheel to column
     def addWheel(self, settings = "", turnOverSymbol = "A"):
          tempRotorWheel = rotorWheel(settings, turnOverSymbol)
          self.rotorColumn.addWheel(tempRotorWheel)
     
     #Add reflectorWheel to the enigma machine
     def addReflector(self, settings = ""):
          self.reflector = reflectorWheel(settings)

#Create Machine A
enigmaMachineA = enigmaMachine()

#Add rotorWheel
enigmaMachineA.addWheel("JGDQOXUSCAMIFRVTPNEWKBLZYH", "Q")
enigmaMachineA.addWheel("NTZPSFBOKMWRCJDIVLAEYUXHGQ", "E")
enigmaMachineA.addWheel("JVIUBHTCDYAKEQZPOSGXNRMWFL", "V")

#Add reflector
enigmaMachineA.addReflector("QYHOGNECVPUZTFDJAXWMKISRBL")


#Create Machine B
enigmaMachineB = enigmaMachine()

#Add rotorWheel
enigmaMachineB.addWheel("JGDQOXUSCAMIFRVTPNEWKBLZYH", "Q")
enigmaMachineB.addWheel("NTZPSFBOKMWRCJDIVLAEYUXHGQ", "E")
enigmaMachineB.addWheel("JVIUBHTCDYAKEQZPOSGXNRMWFL", "V")

#Add reflector
enigmaMachineB.addReflector("QYHOGNECVPUZTFDJAXWMKISRBL")


message = "iloveyou"
print("Message: " + message)

encryptedMessage = enigmaMachineA.encryptStr(message)
print("Encrypted Message: " + encryptedMessage)

decryptedMessage = enigmaMachineB.decryptStr(encryptedMessage)
print("Decrypted Message: " + decryptedMessage)
































