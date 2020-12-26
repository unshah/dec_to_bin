# Function used to get a number from the user
def getInput():
    print("Please enter the decimal number that you want to convert into a binary number: ")
    global dec
    dec = input()

    print(f"The number you entered is: " + dec)
    dec = int(dec)

# Function used to convert the number into a binary one and display it
def convertNum():
    num = bin(dec)

    print("The binary number: " + str(num))

def main():
    #Run getInput function
    getInput()

    #Run convertNum Function
    convertNum()

#Run the main Function
main()
