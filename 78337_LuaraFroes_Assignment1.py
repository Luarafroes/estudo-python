#Luara Froes
#ID: 78337

#listing the blood types
BloodType = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
#listing the blood types to donate to (the first group before the comma is the blood type that can donate to the first blood type in the list "Bloodtype)
CanDonateTo = ["A+, AB+", "A-, A-, AB+, AB-", "B+, AB+", "B+, B-, AB+, AB-", "AB+", "AB+, AB-", "O+, A+, B+, AB+", "Everyone"]
#listing the blood types to receive from
CanReceiveFrom = ["A+, A-, O+, O-", "A-, O-", "B+, B-, O+, O-", "B+, B-", "Everyone", "AB-, A-, B-, O-", "O+, O-", "O-"]

print("\nWelcome to the blood center!")
print("Our porpose is educate patients about blood type compatibility\n")

while True:

#now we will make a menu to ask the user what they want to do

    print("Please select an option:")
    print("1. Check blood type I can donate to")
    print("2. Check blood type I can receive from")
    print("3. Exit")
    choice = input("Enter your choice: ") #this will ask the user to enter a number from 1 to 3
    if choice == "1":
        userbloodtype = input("Please enter your blood type: ") #this will ask the user to enter their blood type
        if userbloodtype in BloodType: #this will check if the blood type is in the list of blood types
            for i in range(len(BloodType)): 
                if userbloodtype == BloodType[i]:
                    print("\nThe blood type", userbloodtype, "can donate to: ", CanDonateTo[i]) #this will give the user the blood type they can donate to (if they say the first value from the list "BloodType", it will give the first value from the list "CanDonateTo")

        else:
            print("Invalid blood type. Please try again.") #If the user said something that is not on the list "BloodType", they will get this message
    elif choice == "2":
        userbloodtype = input("Please enter your blood type: ") #this will also ask the user to enter their blood type
        if userbloodtype in BloodType:
            for i in range(len(BloodType)):
                if userbloodtype == BloodType[i]:
                    print("\nThe blood type", userbloodtype, "can receive from: ", CanReceiveFrom[i]) #this will give the user the blood type they can receive from (if they say the first value from the list "BloodType", it will give the first value from the list "CanReceiveFrom")

        else:
            print("Invalid blood type. Please try again.")
    elif choice == "3":
        print("Thank you for using our service!") 
        False #this will end the program



