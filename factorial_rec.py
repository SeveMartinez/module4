def factorial_rec(num):
    if num == 1:
        return 1
    return num*factorial_rec(num-1)

print(factorial_rec(5))

