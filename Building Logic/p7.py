n = int(input("Enter the number of rows: "))

for i in range(0, 5):
    for j in range(n-i-1, 0, -1):
        print(" ", end = " ")
    for k in range(0, (2*i)+1):
        print("*", end = " ")
    for l in range(1, n-i-1):
        print(" ", end = " ")
    print("")