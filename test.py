def check_path(array, row, objective):

    cycle = False

    # Base case, where the path closed.
    if row == objective:
        return True

    for i in range(3):
        if array[i][row]:
            cycle = check_path(array, i, objective)

    if not cycle:
        return False
    else:
        return True


array = []
for i in range(3):
    array.append([False, False, False])

array[0][1] = True
array[2][1] = True
number_edges = 2
# array[2][0] = True
row, column = 2, 0
cycle = False

print(array)

if number_edges < 2:
    array[row][column] = True
else:
    cycle = check_path(array, row, column)

if not cycle:
    array[row][column] = True
    number_edges += 1
print(array)
