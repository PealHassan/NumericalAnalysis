def get_Function_Value(Function, x):
    res = 0.0
    for i in range(len(Function)):
        res += ((x**i)*Function[i]);
    return res

def differentiation(Function):
    for i in range(1,len(Function)):
        Differentiated_Function.append(float(i)*Function[i])

def find_initial_x():
    temp = abs(get_Function_Value(Function,0.0))
    point = 0
    for i in range(-1000000,1000000):
        u = get_Function_Value(Function,float(i))
        v = get_Function_Value(Differentiated_Function,float(i))
        if(v != 0 and abs(u) < temp):
            temp = abs(u)
            point = float(i)
    return point



def newtonRaphsonMethod():
    guess_root = find_initial_x()
    table = []
    iteration = 0
    while True:
        iteration += 1
        if iteration > 1000000:
            return []
        function_value_for_root = get_Function_Value(Function,guess_root)
        u = get_Function_Value(Differentiated_Function,guess_root)
        if(u == 0):
            return []
        table.append([guess_root,abs(function_value_for_root)])
        if(abs(function_value_for_root) <= Error_tolerance):
            print(f"Root For the given Equation with Error Tolerance {Error_tolerance} is : {guess_root}")
            break
        guess_root = guess_root - (function_value_for_root/u)
    return table

if __name__ == '__main__':
    Error_tolerance = 0.0001
    Function = [float(i) for  i in input("Input Function Coefficients : ").split()] # input Function
    Function.reverse()
    Differentiated_Function = []
    differentiation(Function)
    table = newtonRaphsonMethod()
    if(table == []):
        print("No Real Root Exists for The Given Function.")
    else :
        print("{:<30} {:<30} ".format('Root','Error'))
        print("{:<30} {:<30} ".format('-'*30, '-'*30))
        for i in table:
            a,b = i
            print("{:<30} {:<30}".format(a,b))