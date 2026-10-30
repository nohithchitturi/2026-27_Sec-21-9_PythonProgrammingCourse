#operator precedence
a=9
b=7
print(f"result of {a}/{b} is{a/b}")
print(f"result of {a}//{b} is {a//b}")

a=19
b=9
print(f"result of {a}*{b}//2 is {a*b//2}")


a=900
print(f"result of {a}//10//2 is {a//10//2}")

a =69
b=67
print(f"result of {a}+{b}*2**2 is {a+b*2**2}")


a=7
b=9
print(f"result of ({a}+{b})*2 is {(a+b)*2} ")

a=5
b=5
print(f"result of {a}+{b}*2>19 is {a+b*2>19}")


a=8
b=5
print(f"result of {a}>{b} and {b}>1 or a<0 is {a>b and b>1 or a<0}")