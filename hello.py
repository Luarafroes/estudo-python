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

print("ola")