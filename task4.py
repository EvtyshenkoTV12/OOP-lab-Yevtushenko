import argparse


def optimal_weight(W, w):
    golds = [0] + w
    gold_dict = {}
    for i in range(0, W+1):
        gold_dict[(i, golds[0])] = 0
    for i in golds:
        gold_dict[(0, i)] = 0

    for i in range(1, len(golds)):
        for weight in range(1, W+1):
            gold_dict[(weight, golds[i])] = gold_dict[(weight, golds[i-1])]
            if golds[i] <= weight:
                val = gold_dict[(weight-golds[i], golds[i-1])] + golds[i]
                if gold_dict[(weight, golds[i])] < val:
                    gold_dict[(weight, golds[i])] = val

    return max(gold_dict.values())


parser = argparse.ArgumentParser(description="Input for knapsack problem")
parser.add_argument("-W", type=int, help="Capacity")
parser.add_argument("-w", nargs="+", type=int, help="Weights")
parser.add_argument("-n", type=int, help="Amount of bars")
input_args = parser.parse_args()
capacity = input_args.W
weights = input_args.w
bars_amount = input_args.n

if not bars_amount == len(weights):
    raise ValueError("Arguments are incorrect")
else:
    weight = optimal_weight(capacity, weights)
    print(weight)
