def mikstura(x,x1,y,y1,z,z1):
    a=x-x1
    b=y-y1
    c=z-z1
    lista = [a,b,c]
    return lista
def vectors_to_matrix(vectors):
    matrix = []
    for vector in vectors:
        matrix.append(vector)
    return matrix
def matrix_mult(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_product = 0
            for k in range(len(B)):
                sum_product += A[i][k] * B[k][j]
            row.append(sum_product)
        result.append(row)
    return result
all_results = []
print ("start programu /alchemia in shallow/")
cycle = int(input("insert number of cycles"))
while cycle > 0:
    red= int(input("insert red elements"))
    green = int(input("insert green elements"))
    yellow = int(input("inster yellow elements"))
    blue = int(input("insert blue elements"))
    white = int(input("insert white elements"))
    black = int(input("insert black elements"))
    result = mikstura(red,green,yellow,blue,white,black)
    all_results.append(result)
    print("you have:",result)
    cycle -= 1

print("All results:", all_results)
while True:
    print("\nChoose sorting option:")
    print("1. Reverse order")
    print("2. Sort by first element")
    print("3. Sort by magnitude")
    print("4. Keep original order")
    print("5. custom order")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        all_results.reverse()
        print("Reversed:", all_results)
    elif choice == "2":
        all_results.sort(key=lambda x: x[0])
        print("Sorted by first element:", all_results)
    elif choice == "3":
        all_results.sort(key=lambda x: sum(i**2 for i in x)**0.5)
        print("Sorted by magnitude:", all_results)
    elif choice == "4":
        print("Original:", all_results)
    elif choice == "5":
        custom_order = []
        for i in range(len(all_results)):
            index = int(input(f"Enter index of element {i+1} (0 to {len(all_results)-1}): "))
            custom_order.append(all_results[index])
        all_results = custom_order
        print("Custom ordered:", all_results)
    elif choice == "6":
        break
    else:
        print("Invalid choice")