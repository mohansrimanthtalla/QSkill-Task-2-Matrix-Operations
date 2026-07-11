import numpy as np

matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[5, 6],
                    [7, 8]])

while True:
    print("\n========== Matrix Operations Tool ==========")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Matrix Transpose")
    print("5. Matrix Determinant")
    print("6. Show Matrices")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        print("\nMatrix Addition:")
        print(matrix1 + matrix2)

    elif choice == "2":
        print("\nMatrix Subtraction:")
        print(matrix1 - matrix2)

    elif choice == "3":
        print("\nMatrix Multiplication:")
        print(np.dot(matrix1, matrix2))

    elif choice == "4":
        print("\nTranspose of Matrix 1:")
        print(matrix1.T)

    elif choice == "5":
        print("\nDeterminant of Matrix 1:")
        print(np.linalg.det(matrix1))

    elif choice == "6":
        print("\nMatrix 1:")
        print(matrix1)
        print("\nMatrix 2:")
        print(matrix2)

    elif choice == "7":
        print("\nThank you for using Matrix Operations Tool!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 7.")