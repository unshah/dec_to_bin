# Function used to get a number from the user
def getInput():
    print("Please enter the number or string that you want to convert into a binary number: ")
    global a
    a = input()

    print(f"The number or string you entered is: " + a)


# Function used to convert the number into a binary one and display it
def convertNum():
    dec = int(a)
    num = bin(dec)

    print("The binary number: " + str(num))

#Function used to conver string to binary.
def convertStr():
    out = ''.join(format(ord(x),'b') for x in a)

    print("The converted string is: " + out)

def main():
    #Run getInput function
    getInput()

    try:
    #Run convertNum Function
        convertNum()
    #if convertNum gives an error then use convertStr
    except:
        convertStr()

#Run the main Function
main()
