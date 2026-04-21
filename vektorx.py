def mikstura(x, x1, y, y1, z, z1):
    """
    Returns a vector [a, b, c]
    """
    a = x - x1
    b = y - y1
    c = z - z1
    return [a, b, c]


# Matrix where each row is a vector
matrix = []

print("start programu / alchemia in shallow /")
cycle = int(input("insert number of cycles: "))

while cycle > 0:
    red = int(input("insert red elements: "))
    green = int(input("insert green elements: "))
    yellow = int(input("insert yellow elements: "))
    blue = int(input("insert blue elements: "))
    white = int(input("insert white elements: "))
    black = int(input("insert black elements: "))

    vector = mikstura(red, green, yellow, blue, white, black)

    # add vector as a NEW ROW in the matrix
    matrix.append(vector)

    print("vector added:", vector)
    cycle -= 1


print("\nMatrix (rows = vectors):")
for row in matrix:
    print(row)


# -------- Sorting menu --------
while True:
    print("\nChoose sorting option:")
    print("1. Reverse order (rows)")
    print("2. Sort by first element")
    print("3. Sort by vector magnitude")
    print("4. Keep current order")
    print("5. Custom row order")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        matrix.reverse()
        print("Reversed matrix:", matrix)

    elif choice == "2":
        matrix.sort(key=lambda row: row[0])
        print("Sorted by first element:", matrix)

    elif choice == "3":
        matrix.sort(key=lambda row: sum(v**2 for v in row) ** 0.5)
        print("Sorted by magnitude:", matrix)

    elif choice == "4":
        print("Current matrix:", matrix)

    elif choice == "5":
        custom_matrix = []
        for i in range(len(matrix)):
            index = int(input(
                f"Enter index for row {i+1} (0 to {len(matrix)-1}): "
            ))
            custom_matrix.append(matrix[index])

        matrix = custom_matrix
        print("Custom ordered matrix:", matrix)

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice")
