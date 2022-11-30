import Gaussian
def Input():
    print("Warning : number of rows should be equal to number of columns")
    row = int(input("Number of Rows : "))
    col = int(input("Number of Columns : "))
    matrix = []
    for i in range(row):
        temp = [float(i) for i in input().split()]
        matrix.append(temp)
    return matrix

def Inverse(matrix):
    n = len(matrix)
    inv = []
    for i in range(n):
        temp = [0.0 for i in range(n) ]
        inv.append(temp)
    for i in range(n):
        temp = []
        for j in range(n):
            temp2 = matrix[j].copy()
            if(i == j): temp2.append(1)
            else: temp2.append(0)
            temp.append(temp2)
        ans = Gaussian.start(temp)
        if(ans == None):
            print('Inverse Matrix is not possible.')
            break
        for j in range(n):
            inv[j][i] = ans[j]
    return inv


if __name__ == '__main__':
    matrix = Input()
    inverse = Inverse(matrix)
    print(inverse)
