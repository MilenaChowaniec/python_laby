import random

def randomize(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] = random.random() # returns random float num between (0,1)
        
# print 2D array
def print_tab2(tab):
     for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(round(tab[i][j], 2), end="")
            print(', ', end='')
        print()
        
# print 1D array
def print_tab(tab):
    for i in range(len(tab)):
        print(round(tab[i], 2), sep=', ', end=' ',)
        
# find min element in each row
def find_min_elem_idx(M):
    A = []
    for i in range(len(M)):
        min_val = 1
        idx = 0
        for j in range(len(M[i])):
            if min_val > M[i][j]:
                min_val = M[i][j]
                idx = j
        A.append(idx)
    return A

# find max element in each column
def find_max_elem_idx(M):
    B = []
    for i in range(len(M[0])):
        max_val = -1
        idx = 0
        for j in range(len(M)):
            if max_val < M[j][i]:
                max_val = M[j][i]
                idx = j
        B.append(idx)
    return B
     
def find_min_elem(M, A):
    min_val = 1
    for i in range(len(M)):
        if min_val > M[i][A[i]]:
            min_val = M[i][A[i]]
    print("\nMin value: ", min_val)
    
def find_max_elem(M, B):
    max_val = -1
    for i in range(len(M[0])):
        if max_val < M[B[i]][i]:
            max_val = M[B[i]][i]
    print("\nMax value: ", max_val)
       
# array size
row = 4
column = 6

M = [[0] * column for _ in range(row)]

randomize(M);
print("Array M: ")
print_tab2(M)
A = find_min_elem_idx(M)
print("\nArray A: ")
print_tab(A)
B = find_max_elem_idx(M)
print("\n\nArray B: ")
print_tab(B)
find_min_elem(M, A)
find_max_elem(M, B)




    
    


