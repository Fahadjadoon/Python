#conditionals statments

#if statment
x = 10
if x > 5:
    print("x is greater than 5")

#else-if
x = 10
if x > 15:
    print("x is greater than 15")
else:
    print("x is not greater than 15")

#elif
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")

#0 is evaluated to false
#Any empty bracket will evaluate to false (), {}, []