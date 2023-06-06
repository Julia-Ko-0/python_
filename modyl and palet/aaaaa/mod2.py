def bozmog_treygol(a,b,c):
    if  a<(b+c) or b<(a+c) or c<(a+b ):
        

    
        if a == b and b == c:
                    
            print("Треугольник равностооронней ")
        elif a == c: 
            print("Треугольник равнобедренный " )
        elif a == b and a != c :
            print("Треугольник равнобедренный ")
        elif c == b and a != b :
                    
            print ("Треугольник равнобедренный " )

        else :
            
            print("Треугольник разносторонний " )
    else:
        print("невозможный треугольник")
        
