def print_diamond(n):
    middle = (n + 1) // 2
    
    for i in range(1, middle + 1):
        num_stars = 2 * i - 1
        num_spaces = middle - i
        print(" " * num_spaces + "*" * num_stars)

    for i in range(middle - 1, 0, -1):
        num_stars = 2 * i - 1
        num_spaces = middle - i
        print(" " * num_spaces + "*" * num_stars)

def getDiamondInfo():
    n = int(input("Enter a natural number: "))

    if n > 0:
        print_diamond(n)
    else:
        print("Please enter a natural number greater than zero.")

getDiamondInfo()