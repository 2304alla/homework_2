# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num = input('Введите вещественное число: ')
# sum=0

# for i in num:
#     if i.isdigit():
#         sum+=int(i)
       
# print (sum)        
        
        
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input("Введите число: "))
# temp=1
# for i in range(1,num+1):
#     temp=temp*i
#     print(temp,)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

# n=int(input())
# dict = {}
# sum=0
# for i in range(1,n+1):
#     dict[i] = round((1+1/i)**i,2)
    
    
# for i in dict.values():
#     sum+=i    
    
# print(dict) 
# print(sum)   


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n=int(input())
list_number=[i for i in range(-n,n+1)]
print(list_number)


file = open ("file.txt","r")


for i in file:
    print (int(i))
    
result=1

for i in range(len(file)):
    result*= list_number[file[i]]  
print(result)    

# list_number = list(map(strip,file))
# print(list_number)