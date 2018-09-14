# PyEnigmaMachine

This is a simple implementation of the Enigma Machine in python. It should be mostly correct though double step sequence is not implemeneted. I used standard settings from the German Railway (Rocket) model.

Usage is as following:
```python
#Create Machine A
enigmaMachineA = enigmaMachine()

#Add rotorWheel
enigmaMachineA.addWheel("JGDQOXUSCAMIFRVTPNEWKBLZYH", "Q")
enigmaMachineA.addWheel("NTZPSFBOKMWRCJDIVLAEYUXHGQ", "E")
enigmaMachineA.addWheel("JVIUBHTCDYAKEQZPOSGXNRMWFL", "V")

#Add reflector
enigmaMachineA.addReflector("QYHOGNECVPUZTFDJAXWMKISRBL")


#Create Machine B with same settings
enigmaMachineB = enigmaMachine()

#Add rotorWheel
enigmaMachineB.addWheel("JGDQOXUSCAMIFRVTPNEWKBLZYH", "Q")
enigmaMachineB.addWheel("NTZPSFBOKMWRCJDIVLAEYUXHGQ", "E")
enigmaMachineB.addWheel("JVIUBHTCDYAKEQZPOSGXNRMWFL", "V")

#Add reflector
enigmaMachineB.addReflector("QYHOGNECVPUZTFDJAXWMKISRBL")

#Communication
message = "iloveyou"
print("Message: " + message)

encryptedMessage = enigmaMachineA.encryptStr(message)
print("Encrypted Message: " + encryptedMessage)

decryptedMessage = enigmaMachineB.decryptStr(encryptedMessage)
print("Decrypted Message: " + decryptedMessage)
```
