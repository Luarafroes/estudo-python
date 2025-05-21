#print("Hi Luara")
#print("Hello world")
#print("The itsy bitsy spider climbed up the waterspout")
#print()
#print("Down came the rain and washed the spider out")
#print("The itsy bitsy spider\nclimbed up the waterspout")
#print()
#print("Down came the rain\nand washed the spider out")
#print("Luara\'Froes")  #a barra faz com que o python entenda que a proxima aspas e parte da frase
#print("Hello\r world") #a barra com r serve para apagar o que esta antes dela
#print("Hello\t world") #a barra com t serve para dar um espaco entre as palavras 
#print("Hello\n world") #a barra com n serve para pular uma linha
#print("The itsy bitsy spider", "climbed up", "the waterspout")
#print("My name is", "Python.", end=" ")
#print("Monty Python") 
#print("My name is", "Python.", end="\n")
#print("Monty Python")
#print("My", "name", "is", sep="_", end="*")
#print("Monty", "Python.", sep="*", end="*\n")
#print("My_name_is*Monty*Python*")
#print("Programming", "Essentials", "in", sep="***", end="...")
#print("Python")
#print("Programming", "Essentials", "in", sep="\n", end="...")
#print("Python")
#print("I'm", "learning", "Python")
#print ('"I\'m"\n""learning""\n"""Python"""') 
#print(True > False)
#print(True<False)
#print(2 ** 3)
#print(2. ** 3)
#print(2 ** 3.)
#print(2. ** 3.)
#print(6/3)
#print(6/3.)
#print(6./3)
#print(6./3.)
#print(7/3)
#print(-6//4)
#print(6.//-4)
#Adiós_Señora = 3
#var = 1
#account_balance = 1000.0
#client_name = 'John Doe'
#print(var, account_balance, client_name)
#print(var)
#var = 2
#print (var)
#var = '3.8.5'
#print ("python version:" + var)
#print ("Luara" + account_balance)
#var = 100
#print(var)
#var = 200 + 300
#print(var+var)
#a = 3.0
#b = 4.0 
#c = (a**2 + b**2)**0.5
#print(c)
#johns_apples = 3
#marys_apples = 5
#Adans_apples = 6
#print(johns_apples, marys_apples, Adans_apples, sep=",") 
#total_apples = johns_apples+marys_apples+Adans_apples
#print (total_apples)
#print("total number of apples:" , total_apples)
#i= 1
#var= 2
#rem= 3
#j = 2
#x = 1
#i += 2*j
#var /= 2
#rem %= 10
#j-=(i+var+rem)
#x **=2
#print (i, j, var, rem, x)
#print (i+j)
'''kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/ 1.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
print("bla bla bla")''' #voce pode comentar assim usando hashtag ou usando os 3 pontinhos um no comeco e outro no final
'''print("Tell me anything...")
anything = input()
print("Hmm...", anything, "...Really?")'''
'''anything = input("enter a number: ")
something = int(anything) ** 2.0 
print(anything, "to the power of 2 is", something)'''#int significa mudar o string(frase) para integer(number), e tbm pode usar "float" para mudar para numero com . ex:1.5
'''print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")'''
'''n= int (input())
print(n>=100)
print(int(input()) >=100)'''




#if else staments 
'''number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third1 number: "))

if number1 > number2:
    larger_number = number1
elif number3 > number1:
    larger_number = number3
else:
    larger_number = number2
    

print("the larger number is:", larger_number)'''

'''PIT = float(input("Enter the value: "))



if PIT <= 85528: 
    tax =  PIT*18 - 556.02
else:
    tax = (PIT-85528)*32 + 14839

tax = round(tax, 0)

print (tax)'''

'''moneyInMypocket = 100.

while moneyInMypocket > 0:

    what_drink_do_you_want = (input("what do you wnat to drink?: "))
    how_much_it_is = int(input("Enter the price: "))
    if moneyInMypocket>= how_much_it_is:
        print ("here is your drink" , what_drink_do_you_want)
        moneyInMypocket -= how_much_it_is
        print ("the amount of money left is: ", moneyInMypocket)
    else:
        print("Sorry I dont have more money for this")
    
else:
    print ("now I dont have more money, Im going home sad")'''


'''secretnumber = 510
i = 0

print("Welcome to my game, muggle!")
print("Try to guess the secret number")
guess = int(input("Guess what is the secret number: "))
while guess != secretnumber: 
    print("Ha ha! You're stuck in my loop!")
    guess = int(input("Try again: "))
    i += 1

print("Well done, muggle! You are free now.")
print("Number of attempts:", i)'''

'''import time
for Mississippi in range(1, 6):
    print (Mississippi , "mississippily")
    time.sleep (3)
print("Ready or not, here I come!")'''


#praticando type (type faz com q mostre o tipo da variavel q estou usando)
'''x = 10
print(type(x))'''
'''if type(x) == float:
    print("x is a float")
else: 
    print("x is not a float")'''

# list is a collection which is ordered and changeable. Allows duplicate members. is represented by [], the itens are separate by a , (coma) and can have any type of data
'''mylist = [0,8,3,1,6,5,5,5,7,8]
print(mylist)

print(mylist[8]) #print the 9th element of the list (the first element is 0)
print(mylist[-1]) #print the last element of the list
print(mylist[2:5]) #print the 3rd to the 5th element of the list
print(mylist[5:]) #print from the 6th element to the end of the list
print(mylist[:5]) #print from the first element to the 5th element of the list'''

#len function is used to get the length of the list (tamanho da lista) ou quantos elementos tem na lista
'''print(len(mylist))''' #print the length of the list (how many elements have in the list)

#del function is used to delete an element of the list 
'''del mylist[0] '''#delete the first element of the list
'''print(mylist)'''

#Lab about list
'''Hat = [1,2,3,4,5]
print(Hat)
Hat[2] = int(input("enter a number to replace the middle number: "))''' #this will replace 3 for the number that the user will enter
'''print(Hat) 
print("now I will delete the last element of the list")

del Hat[4] #this will delete the last element of the list
print(Hat)

print("the numbers of elements on this list is:", len(Hat))''' #this will print the length of the list'''

#methods is a function that belongs to an object, in this case the object is the list
#append method is used to add an element to the end of the list (is represented by "name of the list".append)
'''
list = [1,2,3,4,5]
list.append(6)
print(list)'''

#insert method is used to add an element to a specific position of the list (is represented by "name of the list".insert(position, element))

'''mylist = []
for i in range(5):
    mylist.insert(0, i+1)''' #this will add the numbers 1 to 5 in the list in the position 0

'''print(mylist)''' #this will print the list with the numbers 1 to 5 in the position 0 of the list = [5,4,3,2,1]

#Lab about list methods append and insert

'''Beatles = []
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print(Beatles)
for i in range(2):
    Beatles.append(input("enter the name of the next member of the Beatles: "))
print(Beatles)
del Beatles[len(Beatles)-1] #this will delete the last element of the list #del is a function that is used to delete an element of the list
del Beatles[len(Beatles)-1] #this will delete the last element of the list again
print(Beatles)
Beatles.insert(0, "Ringo Starr")
print(Beatles)'''

'''mylist = ['white', 'blue', 'red', 'green', 'yellow']

for i in range(5): #this will print the numbers from 0 to 4
    print(mylist[i]) #this will print the colors in the list'''

#voce pode colocar uma lista dentro de outra lista e ela sera chamada de lista aninhada (nested list) e a lista dentro da lista se torna um unico elementp
#exemplo:
'''mylist = [1,2,3,4,5,[6,7,8,9]]'''   #this will create a list with 5 elements and the last element is a list with 4 elements


'''list = [8,10,6,2,4]
for a in range(len(list)-1): 
    for i in range(len(list)-1): #this will print the numbers from 0 to 3 (the length of the list -1)
        if list[i] > list[i+1]: #this will check if the first element is greater than the second element
            list[i], list[i+1] = list[i+1], list[i] #this will swap the elements of the list if the first element is greater than the second element
         
    print(list) #this will print the list after the swap'''
#input is a function that is used to get the input from the user, in this case the user will have to press enter to continue the loop'''
'''sum = 0
for i in range(10):
   #print(i+1)
    sum =sum + i
    print("the sum is:", sum)'''

'''sum = 0
for i in range(30):
    sum = sum + i+1
print("the sum is:", sum)

sum = 0
for i in range(50):
    sum = sum + i+1
print("the sum is:", sum)'''


# print("Hello world" end=)
 
# def MyFunction (Anumber):
#     sum = 0
#     for i in range(Anumber):
#         sum = sum + i+1
#     print("the sum between 1 and" , Anumber , "is:", sum)

#     MyFunction(int(input("enter a number: "))) #this will call the function MyFunction and will pass the number that the user will enter as a parameter to the function
# # this will print the sum between 1 and the number that the user will enter

#     def message (what, number):
#     print("Enter", what, "number", number)

#     message("thelephone",11)
#     message("price",5)
#     message("number", 5)
    
#     def MyFunction (Anumber):
#         sum = 0
#     for i in range(Anumber):
#         sum = sum + i+1
#     print("the sum between 1 and" , Anumber , "is:", sum)

#     MyFunction(int(input("enter a number: "))) #this will call the function MyFunction and will pass the number that the user will enter as a parameter to the function
# this will print the sum between 1 and the number that the user will enter

