rows = int(input("Enter number of rows: "))
for row_loop_var in range(rows, 0, -1):
    for column_loop_var in range(1, row_loop_var + 1):
        print("*", end=" ")
    print()