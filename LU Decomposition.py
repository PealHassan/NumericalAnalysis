def Input():
    print("Warning : number of rows should be equal to number of columns")
    row = int(input("Number of Rows : "))
    col = int(input("Number of Columns : "))
    matrix = []
    for i in range(row):
        temp = [float(i) for i in input().split()]
        matrix.append(temp)
    return matrix


def findLTandUT(matrix):
    signL = []
    signU = []
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        templ = []
        tempu = []
        for j in range(col):
            if(i == j):
                templ.append(1)
                tempu.append(0)
            elif i < j:
                templ.append(1)
                tempu.append(0)
            else:
                templ.append(0)
                tempu.append(1)
        signL.append(templ)
        signU.append(tempu)

    ansL = []
    ansU = []
    for i in range(row):
        ansL.append([0.0 for i in range(col)])
        ansU.append([0.0 for i in range(col)])
    for i in range(row):
        for j in range(col):
            if i == j:
                ansL[i][j] = 1.0
    for i in range(row):
        for j in range(col):
            sum = 0.0
            for k in range(row):
                if signL[i][k] == 0:
                    sum = matrix[i][j] - sum
                    sum/=ansU[k][j]
                    ansL[i][k] = sum
                    signL[i][k] = 1
                    break
                elif signU[k][j] == 0:
                    sum = matrix[i][j] - sum
                    sum/=ansL[i][k]
                    ansU[k][j] = sum
                    signU[k][j] = 1
                    break
                else:
                    sum += (ansL[i][k] * ansU[k][j])
    return ansL, ansU






if __name__ == '__main__':
    matrix = Input()
    lowerT, upperT = findLTandUT(matrix)
    print("Lower Triangle : ")
    for i in lowerT:
        print(i)
    print("Upper Triangle : ")
    for i in upperT:
        print(i)


