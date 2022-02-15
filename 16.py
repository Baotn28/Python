def different(n):
    if n <= 17:
        return 17 - n
    else:
        return (n-17) * 2

# print(different(22))
m = int(input("Input an integer: "))
print(different(m))
