#Write a python program for contact tracing:

#Step projection:
#create a working dictionary
#create an input collector from the user and stores the info in the dictionary
#print the output using 'for'
#create a main menu for the whole program
#insert the program into a while loop, integrating the exit function

#Main Dictionary for Contact Persons and their infos will be stored here
contactPersons={}

#While loop for continuing program
while True:
    #Menu Design interface
    print("///////////////////////////")
    print("  CONTACT TRACER PROGRAM")
    print("///////////////////////////")
    print("\n///////////////////////////")
    print("Welcome to the Main Menu!")
    print("\nThese are your options: ")
    print("(1) Add a contact")
    print("(2) Search for a contact")
    print("(3) Exit the program")
    print("///////////////////////////")
    #Option selector
    userOption=(input("\nSelect your option (1-3): "))

    #Option 1: Asks for the details of the person to be added then stores it into the variables below
    if userOption=='1':
        print("//////////////////////////////////////////////////////")
        contactName=input("Please enter your full name: ")
        contactAge=int(input("Enter your age: "))
        contactNumber=int(input("Enter your contact number: "))
        contactAddress=input("Enter your present address: ")
        contactVax=input("Please state if you have been vaccinated already (Yes)/(No): ")
        print("\nThank you! Process Done.")
        print("//////////////////////////////////////////////////////")

        #The variables are now stored in the main dictionary and are all under the 'Name' the user inputted, much like a folder
        contactPersons[contactName]={}
        contactPersons[contactName]['Full name']=contactName
        contactPersons[contactName]['Age']=contactAge
        contactPersons[contactName]['Contact Number']=contactNumber
        contactPersons[contactName]['Present Address']=contactAddress
        contactPersons[contactName]['Vaccine Status']=contactVax

    #Option 2: It searches the person inputted by the user and returns the values inputted earlier
    elif userOption=='2':
        print("///////////////////////////")
        contactSearch=input("Enter the full name of your desired contact: ")
        print()
        #if statement to determine contact person exists
        if contactSearch in contactPersons:    
            #for loop for successful printing the key and value of the Contact person located      
            for searchedName, searchedValues in contactPersons.items():
                if contactSearch==searchedName: 
                    for nameKey in searchedValues:
                        print(nameKey,':',searchedValues[nameKey])
                        print("///////////////////////////")

        #Warning message
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Incorrect input or Contact person does not exist.")
            print("Please check your spelling and try again.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    #Final prompt after finished inputting
    print("!******************************************************!")
    #user will be prompted to enter 'y' or 'n' for the loop to continue or stopped
    programPrompt=input("   Do you want to continue with the program? (y)/(n): ")
    if programPrompt=="n":
        print("     Thank you, come again")
        break
