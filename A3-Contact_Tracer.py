#Write a python program for contact tracing:

#Step projection:
#create a working dictionary
#create an input collector from the user and stores the info in the dictionary
#print the output using 'for'
#create a main menu for the whole program
#insert the program into a while loop, integrating the exit function

contactPersons={}

userOption=(input("Select your option: "))

if userOption=='1':
    contactName=input("Please enter your full name: ")
    contactAge=int(input("Enter your age: "))
    contactNumber=int(input("Enter your contact number: "))
    contactAddress=input("Enter your present address: ")
    contactVax=input("Please state if you have been vaccinated already (Yes)/(No): ")

    contactPersons[contactName]={}
    contactPersons[contactName]['Full name']=contactName
    contactPersons[contactName]['Age']=contactAge
    contactPersons[contactName]['Contact Number']=contactNumber
    contactPersons[contactName]['Present Address']=contactAddress
    contactPersons[contactName]['Vaccine Status']=contactVax

elif userOption=='2':
    contactSearch=input("Enter the full name of your desired contact: ")
    if contactSearch in contactPersons:          
        for searchedName, searchedValues in contactPersons.items():
            if contactSearch==searchedName: 
                for nameKey in searchedValues:
                    print(nameKey,':',searchedValues[nameKey])

#for key, value in contactPersons:
	#print(key, “ : ”, value)


