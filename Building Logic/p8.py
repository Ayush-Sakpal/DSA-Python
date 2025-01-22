n = int(input("Enter the number of rows: "))

for i in range(n, -1, -1):
    for j in range(0, n-i):
        print(" ", end=" ")
    for k in range(1, (2*i)+2):
        print("*", end=" ")
    for l in range(n-i-1, 0, -1):
        print(" ", end=" ")
    print("")