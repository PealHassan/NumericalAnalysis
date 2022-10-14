
def get_Function_Value(x):
    res = 0.0
    for i in range(len(Function)):
        res += ((x**i)*Function[i]);
    return res
def initial_range_left():
    for i in range(-1000000,1000000):
        if(get_Function_Value(float(i)) < 0.0):
            return float(i)
    return 0.0

def initial_range_right():
    for i in range(-1000000,1000000):
        if(get_Function_Value(float(i)) > 0.0):
            return float(i)
    return 0.0

def bisectionMethon():

    Range_Left = initial_range_left()
    Range_Right = initial_range_right()
    table = []
    iteration = 0


    while True:
        iteration += 1
        guess_root = (Range_Left  + Range_Right)/2
        table.append([Range_Left,Range_Right,get_Function_Value(Range_Left),get_Function_Value(Range_Right),guess_root,abs(get_Function_Value(guess_root))])
        function_value_for_root = get_Function_Value(guess_root)
        if(abs(function_value_for_root) <= Error_tolerance):
            print(f"Root For the given Equation with Error Tolerance {Error_tolerance} is : {guess_root}")
            break;
        if(iteration > 1000000):
            return []
        function_value_for_Range_Left = get_Function_Value(Range_Left)
        function_value_for_Range_Right = get_Function_Value(Range_Right)
        if(function_value_for_Range_Left*function_value_for_root <= 0):
            Range_Right = guess_root
        else:
            Range_Left = guess_root
    return table


if __name__ == '__main__':
    Error_tolerance = 0.0001
    Function = [float(i) for  i in input("Input Function Coefficients : ").split()] # input Function
    Function.reverse()
    table = bisectionMethon()
    if(table == []):
        print("No Real Root Exists for The Given Function.")
    else :
        print("{:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format('A', 'B','f(A)', 'f(B)', 'Root', 'Error'))
        print("{:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format('-' * 30, '-' * 30, '-' * 30, '-' * 30, '-' * 30,'-' * 30))
        for i in table:
            a,b,c,d,e,f = i
            print("{:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format(a,b,c,d,e,f))





