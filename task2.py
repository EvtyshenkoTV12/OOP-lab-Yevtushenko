import argparse
import operator

parser = argparse.ArgumentParser(description="Calculate")
parser.add_argument("operator_func", type=str)
parser.add_argument("x", type=int)
parser.add_argument("y", type=int)
args = parser.parse_args()
func = getattr(operator, args.operator_func, None)
try:
    print(func(args.x, args.y))
except:
    print("Error")
