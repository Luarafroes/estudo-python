# from datetime import * # Importando o modulo date do pacote datetime
# today = date.today()
# print("current year:", today.year)
# print("current month:", today.month)
# print("current day:", today.day)

# import math
# print("pi:", math.pi)

# pi = 3.14 #vc pode usar o verbo com o mesmo nome q nao vai dar erro
# print(pi) #seu verbo pi
# print("pi:", math.pi) #pi do modulo math

# for name in dir(math):
#     print(name, end="\t") #mostra todos os nomes do modulo math


# for name in dir(datetime):
#     print(name, end="\t") #mostra todos os nomes do modulo datetime

# print(pow(math.e, 1) == math.exp(math.log(math.e))) #mostra se a potencia de e elevado a 1 é igual a exponencial do logaritmo de e
# print(pow(2,2) == math.exp(2*math.log(2))) #mostra se a potencia de 2 elevado a 2 é igual a exponencial do logaritmo de 2
# print(math.log(math.e, math.e) == math.exp(0)) #mostra se o logaritmo de e na base e é igual a exponencial de 0

# from random import randrange, randint, random, choice, sample


# # for i in range(5):
# #     print(randrange(1, 10)) #gera um numero aleatorio entre 1 e 10

# euromillion = list(range(1, 51))
# luckynumbers = list(range(1, 13))

# print(sample(euromillion, 12))  # escolhe 12 elementos aleatorios da lista
# print(sample(luckynumbers, 2))  # escolhe 2 elementos aleatorios da lista
    
from platform import platform 
print(platform())  # mostra a plataforma do sistema operacional
print(platform(1))  # mostra a plataforma do sistema operacional com a versão
print(platform(0, 1))  # mostra a plataforma do sistema operacional com a versão
 

      