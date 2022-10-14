import sys

def Input():
    print("Number of Equations : ",end=' ')
    n = int(input())
    print("Give me A set of linear Equations : ")
    data = []
    for i in range(n):
        temp = [float(j) for j in input().split()]
        data.append(temp)
    return data


def NaiveGaussianEliminationMethod():
    for i in range(Number_of_Equation-1):
        for j in range(i+1, Number_of_Equation):
            fact = (Equation_Matrix[j][i]/Equation_Matrix[i][i])
            for k in range(Number_of_Equation+1):
                Equation_Matrix[j][k] -= (fact*Equation_Matrix[i][k])

    ans = [0.0 for i in range(Number_of_Equation)]
    for i in Equation_Matrix:
        print(i)
    for i in range(Number_of_Equation-1,-1,-1):
        if Equation_Matrix[i][i] <= Error_Accept:
            print('Math Error.')
            return
        ans[i] = Equation_Matrix[i][Number_of_Equation]/Equation_Matrix[i][i]
    for i in ans:
        print(i)





if __name__ == '__main__':
    Equation_Matrix = Input()
    Error_Accept = 0.0000000001
    Number_of_Equation = len(Equation_Matrix)
    NaiveGaussianEliminationMethod()

    