#Nonlocal

def funcion_a():
    x = 2
    print(x )
    def funcion_b():
        x = 20
        print(x)
    funcion_b(x)
funcion_a