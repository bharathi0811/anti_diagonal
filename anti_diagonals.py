
def anti_diagonals(l):
    r = len(l)
    c = len(l[0])
    for x in range(c - 1):
        i = 0
        j = x
        empty = []
        while i < c and j >= 0:
            empty.append(l[i][j])
            i += 1
            j -= 1
        print(empty)
    for y in range(r):
        j = c - 1
        i = y
        empty_ = []
        while i < r and j >= 0:
            empty_.append(l[i][j])
            i += 1
            j -= 1
        print(empty_)
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries rowwise:")
for i in range(R):
    a =[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
anti_diagonals(matrix)