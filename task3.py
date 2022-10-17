import argparse

def check(formula):
    if not formula[0].isdigit() or not formula[-1].isdigit():
        return False
    for i in range(len(formula) - 1):
        if not formula[i].isdigit() and not formula[i+1].isdigit():
            return False
    return True

parser = argparse.ArgumentParser("Calculate formula")
parser.add_argument("formula", type=str)
args = parser.parse_args()
formula = args.formula
if not check(formula):
    print("False, None")
else:
    print("True,", eval(formula))
