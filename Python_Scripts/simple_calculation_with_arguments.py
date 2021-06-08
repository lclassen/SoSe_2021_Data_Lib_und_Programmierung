# -*- coding: utf-8 -*-

# do simple calculation

"""
This script performs simple calculations.
Arguments are given during the call of the script.
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("number_1", type=int, help="An integer")
parser.add_argument("number_2", type=int, help="Another integer")
parser.add_argument("-multi", default=False, action="store_true")
args = parser.parse_args()

# Commented code, not active anymore
# print(args)
# print(args.number_1, args.number_2)

if args.multi:
    result = args.number_1 * args.number_2
else:
    result = args.number_1 + args.number_2


print(result)

