

open = True  #im using to check if the shop still open
shop = open

while shop == open:  #this is to still asking all the questions untill the person say no
    print("welcome to our shop")

    age = int(input("please enter your age:"))  #this will make the questions
    price = float(input("please enter the price of the product:"))

    if age < 18:  #this will give the discout
        newprice = price/100*90 
        print("it will be" , newprice , "after the discount")
        if newprice > 100:
            print("wait, is more then 100 so you have another discount, now it will", newprice-10)
        else:
            print(newprice)
    else:print(price)
    print("thank you for shopping with us")
    if input("do you want to continue shopping? ") == "no":
        shop = False #this will close the shop and stop the loop
        print("ok, thank you goodbye")
    else:shop = open 
