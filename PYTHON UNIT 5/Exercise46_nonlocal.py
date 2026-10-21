#Nonlocal
x =20
def function_exterior():
    x = 10
    print("Inside the function x = ", x )
    def function_interior():
        x = 30
        print ("Inside the interior function x = ", x)
    function_interior()

function_exterior()