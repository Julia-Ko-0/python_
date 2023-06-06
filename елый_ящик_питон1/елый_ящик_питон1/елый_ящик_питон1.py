from math import sqrt

a = 5
b = 6
c = 7

p = (a + b + c)/2
s = sqrt((p*(p-a)*(p-b)*(p-c)))

if  a<(b+c) or b<(a+c) or c<(a+b ):
    print(s)


    if a == b and b == c:
            
        print("Треугольник равностооронней ")
    elif a == c: 
        print("Треугольник равнобедренный " )
    elif a == b and a != b :
        print("Треугольник равнобедренный ")
    elif c == b and a != b :
            
        print ("Треугольник равнобедренный " )

    else :
        
        print("Треугольник разносторонний " )
else:
    print("невозможный треугольник")
    

        



