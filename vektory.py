def mikstura(x,x1,y,y1,z,z1):
    a=x-x1
    b=y-y1
    c=z-z1
    vektor = [a, b, c]
    return vektor
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
# Function to collect color element values over multiple cycles
def collect_color_elements():
    # Initialize empty list to store all results
    all_results = []
    print("start programu /alchemia in shallow/")
    # Get number of cycles from user
    cycle = int(input("insert number of cycles"))
    # Loop through each cycle
    while cycle > 0:
        red = int(input("insert red elements"))
        green = int(input("insert green elements"))
        yellow = int(input("inster yellow elements"))
        blue = int(input("insert blue elements"))
        white = int(input("insert white elements"))
        black = int(input("insert black elements"))
        # Call mikstura function to create vector from 6 color values
        result = mikstura(red, green, yellow, blue, white, black)
        # Add result to list
        all_results.append(result)
        print("you have:", result)
        cycle -= 1
    # Return list of all results collected
    return all_results


# Function to sort results based on user choice
def sort_results(all_results):
    # Infinite loop for sorting menu - breaks when user chooses to exit
    while True:
        print("\nChoose sorting option:")
        print("1. Reverse order")
        print("2. Sort by first element")
        print("3. Sort by magnitude")
        print("4. Keep original order")
        print("5. custom order")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        # Choice 1: Reverse the order of results
        if choice == "1":
            all_results.reverse()
            print("Reversed:", all_results)
        # Choice 2: Sort by first element of each vector
        elif choice == "2":
            all_results.sort(key=lambda x: x[0])
            print("Sorted by first element:", all_results)
        # Choice 3: Sort by magnitude (Euclidean length) of vectors
        elif choice == "3":
            all_results.sort(key=lambda x: sum(i**2 for i in x)**0.5)
            print("Sorted by magnitude:", all_results)
        # Choice 4: Keep original order (just print)
        elif choice == "4":
            print("Original:", all_results)
        # Choice 5: Custom order - user specifies index of each element
        elif choice == "5":
            custom_order = []
            for i in range(len(all_results)):
                index = int(input(f"Enter index of element {i+1} (0 to {len(all_results)-1}): "))
                custom_order.append(all_results[index])
            all_results = custom_order
            print("Custom ordered:", all_results)
        # Choice 6: Exit the sorting menu
        elif choice == "6":
            break
        else:
            print("Invalid choice")
    # Return sorted results
    return all_results

# Main function that runs the entire program
def main():
    # Collect color elements from user input
    all_results = collect_color_elements()
    # Display all collected results
    print("All results:", all_results)
    # Allow user to sort results in various ways
    all_results = sort_results(all_results)
    # Print final results
    print("Final results:", all_results)

# Only run main() if this file is executed directly (not imported)
if __name__ == "__main__":
    main()