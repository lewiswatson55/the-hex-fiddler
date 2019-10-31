#AQA ASCII-HEX DAT CONVERT PROGRAM THING
#Lewis Watson

#Get Hex Input
print("AQA Simulator HEX String FIDDLER:")
print()
rawhex = input("Enter Converted ASCII >: ")
print()

#Split To Individual Hex Characters
splithex = rawhex.split();
print("Raw Hex Data Split:")
print(splithex)

#Add Leading 00's to make printing valid
while ((len(splithex) % 8) != 0):
    splithex.append('00');

#Pre-Output Message
print()
print("Fiddled with your hex string...")
print()
    

#Loop Through and Pop-Print 4321 Until Empty
j = 0;
sizeofList2 = len(splithex)
while j < sizeofList2 :
   print("dat 0x" + splithex.pop(3) + splithex.pop(2) + splithex.pop(1) + splithex.pop(0))
   j=j+4;


print("0x00")
print()