def MyFunction (Anumber):
    sum = 0
    for i in range(Anumber):
        sum = sum + i+1
    print("the sum between 1 and" , Anumber , "is:", sum)

MyFunction(int(input("enter a number: "))) #this will call the function MyFunction and will pass the number that the user will enter as a parameter to the function
# this will print the sum between 1 and the number that the user will enter
