import random
lista =[1,2,3,4,5]
a= random.randint(5,15)
while True:
    x=int(input("podaj x:"))
    if x>a:
        print("liczba większa od podanej")
    elif x<a:
        print("liczba mniejsza od podanej")
    else:      
        print("zgadłeś")
        break
random.shuffle(lista)
print (lista)

        