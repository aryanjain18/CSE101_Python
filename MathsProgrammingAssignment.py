print("Lets Solve The Homogeneus Equation Ax = 0 :)")
m = int(input("Enter Number Of Rows Of Matrix A = "))
n = int(input("Enter Number Of Coloumns Of Matrix A = "))

#Obviously The Elementary Matrices - Square Matrices Will Be Of Order M x M
list_i = [] #Building Identity Matrix Of Order M
for i in range(m):
    list_i.append([])
for j in range(m):
    for k in range(m):
        if k != j :
            list_i[j].append(0)
        else:
            list_i[j].append(1)

#Row i replace by Row i + C Row j - Identity matrix me E[i][j] = C
def elementary_matrix(i,j,c): #Where, i & j Belong To [1 to M]
    list4 = list_i.copy()
    list4[i-1][j-1] = c
    return list4

def matrix_multiply(list1,list2): #List1 - Matrix 1 - MxN, List2 - Matrix 2 - NxP
    list3 = []
    for i in range(len(list1)):
        list3.append([]) #Make List3 = List1 x List2
    for i in range(len(list1)): #I ranges in M - Selecting Row From First Matrix
        for j in range(len(list2[0])): #J ranges in P - Selecting Column From Second Matrix
            sum = 0
            for k in range(len(list1[0])): #K ranges in N - Selecting Corresponding Elements From Row Of M1 & Coloumn Of M2
                sum += float(list1[i][k])*int(list2[k][j])
            list3[i].append(sum)
    return list3

print("Enter Matrix 'A' - Row-wise, & Entries Seprated By A Space")
list_matrix = [] #Matrix A - M x N
for i in range(n):
    y = list(map(float,input().split()))
    list_matrix.append(y)