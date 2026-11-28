# Example solution: local does not change global
x = 10
def demo():
    x = 20  # local assignment
    print("Inside function, x =", x)
demo()
print("Outside function, x =", x)