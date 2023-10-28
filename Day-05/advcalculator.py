import sys
import calculator as basical

def div(num1, num2):
    d = num1 * num2
    return d

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "div":
    output = div(num1, num2)
    print(output)