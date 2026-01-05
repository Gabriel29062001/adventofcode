# =======================================================================================================================================================
# INITIAL LIBRAIRIES AND VARIABLES
# =======================================================================================================================================================

import numpy as np

code = []
counter_total = 0
counter = 1


with open("input_day_4.txt", "r") as f:
    for line in f:
        code.append(line.strip())

A = np.zeros((len(code), len(code[0])))

def fill_matrix(A, code):
    for i in range(len(code)):
        for j in range(len(code[0])):
            A[i][j] = 1 if code[i][j] == "@" else 0
    return A

A = fill_matrix(A, code)

combinaisons = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
#print(A)
# =======================================================================================================================================================


# =======================================================================================================================================================
# BRUTE FORCE CODE PART 2
# =======================================================================================================================================================
def count_rollpaper_access(A, counter_total):
    counter = 0
    list_index_i = []
    list_index_j = []
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            counter_neighbor = 0
            possible = 1   
            if A[i][j] != 1:
                possible = 0

            for dx,dy in combinaisons:
                ni = i - dx
                nj = j - dy

                if 0 <= ni < A.shape[0] and 0 <= nj < A.shape[1]:
                    if A[ni][nj] == 1:
                        counter_neighbor += 1

                if counter_neighbor >= 4:
                    possible = 0
                    break

            if possible:
                list_index_i.append(i)
                list_index_j.append(j)

                #print(f"{i},{j}")
                counter += 1


    #print(counter)
    counter_total += counter

    return list_index_i, list_index_j, counter, counter_total
# =======================================================================================================================================================



# =======================================================================================================================================================
# MAIN LOOP
# =======================================================================================================================================================
while counter != 0:

    list_index_i, list_index_j, counter, counter_total = count_rollpaper_access(A, counter_total)
    for i,j in zip(list_index_i, list_index_j):
        A[i][j] = 0
print(counter_total)