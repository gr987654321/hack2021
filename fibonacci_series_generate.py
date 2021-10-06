# Program to Generate Fibonaccic series suing recursion

n = int(input("Enter the number of terms of the series : "))
first = 0
second = 1

def gen_fibonacci(n):
    if n <= 1:
        return n
    return gen_fibonacci(n - 1) + gen_fibonacci(n - 2)

for i in range(0, n):
    print(gen_fibonacci(i), end=" ")