import random
i=random.randint(0,100)

for j in range(0,10):
    x=input()
    if int(x)==int(i) :
        j+=1
        break
    
    if int(x)<int(i) :
        print("le nombre est plus grand! ")
    else  :
        print("le nombre est plus petit! ")


if int(x)==int(i) :
    print("Nombre trouvé!!")

if j==9 :
    print("\nNombres de tentatives terminé :(")
