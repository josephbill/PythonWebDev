matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# outer loop
for row in matrix:
    # print(row)
    #inner loop
    for element in row:
        print(element, end=' ')
    print()

# for every outer iteration the set of inner iteration needs to be completed.