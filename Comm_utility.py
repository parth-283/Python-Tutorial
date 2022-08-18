import argparse
import sys


def calc(args_val):
    if args_val.o == 'add':
        return args_val.x + args_val.y
    elif args_val.o == 'mul':
        return args_val.x * args_val.y
    elif args_val.o == 'div':
        return args_val.x / args_val.y
    elif args_val.o == 'sub':
        return args_val.x - args_val.y


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="Enter first number.")
    parser.add_argument('--y', type=float, default=3.0, help="Enter first number.")
    parser.add_argument('--o', type=str, default='add', help="Enter Operation")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
