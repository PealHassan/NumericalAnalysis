def get_Function_Value(x):
    res = 0.0
    for i in range(len(Function)):
        res += ((x**i)*Function[i])
    return res


def find_Upper_Point():
    for i in range(-1000000,1000000):
        if(get_Function_Value(float(i)) > 0.0):
            return float(i)
    return 0.0

def find_Lower_Point():
    dat = 0.0
    for i in range(-1000000,1000000):
        if(get_Function_Value(float(i)) < 0.0):
            dat = float(i)
    return dat

def falsePositionMethod():
    point1x = find_Upper_Point()
    point1y = get_Function_Value(point1x)
    point2x = find_Lower_Point()
    point2y = get_Function_Value(point2x)
    if(point1x > point2x):
        tempx = point1x
        tempy = point1y
        point1x = point2x
        point1y = point2y
        point2x = tempx
        point2y = tempy
    iteration = 0
    table = []
    while True:
        iteration += 1
        guess_root = (point1x*point2y - point2x*point1y)/(point2y-point1y)
        r = get_Function_Value(guess_root)
        table.append([point1x, point1y, point2x, point2y, guess_root, abs(r)])
        if(abs(r) <= Error_tolerance):
            print(f"Root For the given Equation with Error Tolerance {Error_tolerance} is : {guess_root}")
            break
        if(iteration > 1000000):
            return []
        if(point1y*r <= 0):
            point2x = guess_root
            point2y = r
        else:
            point1x = guess_root
            point1y = r



    return table





if __name__ == '__main__':
    Error_tolerance = 0.0001
    Function = [float(i) for i in input("Input Function Coefficients : ").split()]  # input Function
    Function.reverse()
    table = falsePositionMethod()
    if (table == []):
        print("No Real Root Exists for The Given Function.")
    else:
        print("{:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format('Point1X', 'Point1Y', 'Point2x', 'Point2y', 'Root', 'Error'))
        print("{:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format('-'*30,'-'*30,'-'*30,'-'*30,'-'*30,'-'*30 ))
        for i in table:
            a, b, c, d, e, f = i
            print("{:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format(a, b, c, d, e, f))



