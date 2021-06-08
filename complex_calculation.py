# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 08:17:46 2021

@author: User
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("number_1", type=int, help="An integer")
parser.add_argument("number_2", type=int, help="Another integer")
parser.add_argument("--operation", choices=["multi", "sub", "div", "sum"], help="operation you want to execute")

args = parser.parse_args()

# Commented code, not active anymore
# print(args)
# print(args.number_1, args.number_2)

if args.operation == "div":
    result = args.number_1 / args.number_2
elif args.operation == "multi":
    result = args.number_1 * args.number_2
elif args.operation == "sub":
    result = args.number_1 - args.number_2
elif args.operation == "sum":
    result = args.number_1 + args.number_2



print(result)
 
# parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
# parser.add_argument("-multi", default=False, action="store_true")