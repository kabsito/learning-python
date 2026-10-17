x = 8
def plus():
   global x
   x= x + 3*3
   
plus()
print(x)

#Nonlocal

def funcion_a():
    x = 10

    def funcion_b():
        nonlocal x
        x = 20
        print("funcion_b", x)

    funcion_b()
    print("funcion_a", x)
funcion_a