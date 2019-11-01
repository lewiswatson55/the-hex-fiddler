#AQA ASCII-HEX DAT CONVERT PROGRAM THING
#Lewis Watson


#Function to convert ascii to a list of hex values
def asciiToHex(t):

    #Split string input to list
    t = list(t)
    out = ""

    #Loop through and convert each character in list
    for i in range(len(t)):
        out = out + str(hex(ord(t[i])))

    #Remove 0x and Blank Space in Index 0
    out = out.split('0x')
    out.pop(0)

    return out

#Get Hex Input
print("AQA Simulator HEX String FIDDLER:")
print()
string = input("Enter ASCII to be converted to hex and fiddled >: ")
print()

#Split To Individual Hex Characters
splithex = asciiToHex(string);
print("Raw Hex Data Split:")
print(splithex)

#Check if value is exactly divisible and set variable to result
exactlydivisible = 0
if (len(splithex) % 4) == 0: exactlydivisible = 1

#Add Leading 00's to make printing valid
while ((len(splithex) % 4) != 0):
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

if (exactlydivisible): print("dat 0x00")
print()