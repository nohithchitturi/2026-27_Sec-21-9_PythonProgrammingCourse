# Example solution: number right-angled triangle
rows = 6
for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, row_loop_var + 1):
        print(column_loop_var, end=" ")
    print()