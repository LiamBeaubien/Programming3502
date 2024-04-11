#yo yo yo this is Liam

def menu():
    option = input("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit \n\nPlease enter an option: ")
    return option

def encode(x):
    new = ''
    for i in range(len(x)):
        new = new + str((int(x[i])+3)//10)
    return x

#def decode(x):
#wow

option = menu()
if __name__ == "__main__":
    while option!= "3":

        if option == "1":
            encoded = encode(input("Please enter your password to encode: "))
            print(f"Your password has been encoded and stored! \n")
            option  = menu()
        elif option == "2":
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
            option = menu()
