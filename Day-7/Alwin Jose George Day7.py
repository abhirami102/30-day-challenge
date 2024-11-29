num = int(input("Enter a number greater than 1: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"The number {num} is not a prime number.")
            break
    else:
        print(f"The number {num} is a prime number.")
else:
    print("Please enter a number greater than 1.")
