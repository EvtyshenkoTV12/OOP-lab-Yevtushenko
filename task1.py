import argparse

def calculate(x, y, sign):
    if sign == "/":
        if y == 0:
            return None
        return x / y
    elif sign == "*":
        return x * y
    elif sign == "+":
        return x + y
    elif sign == "-":
        return x - y
    else:
        return None

parser = argparse.ArgumentParser(description="Calculate")
parser.add_argument("x", type=int)
parser.add_argument("sign", choices=("+", "-", "*", "/"))
parser.add_argument("y", type=int)
args = parser.parse_args()
result = calculate(args.x, args.y, args.sign)
print(result)