def solve_expression(a, b):

    result = (a - b) + (a * b)
    return result

try:
    a = float(input("What value of 'a' would you like to have?"))
    b = float(input("What value of 'b' would you like to have?"))
    answer = solve_expression(a, b)
    print(f"If your value of a is {a} and b is {b}, the equation of (a - b) + (a * b) is equal to {answer}")

except ValueError:
    print("You need an actual number for both 'a' and 'b'.")