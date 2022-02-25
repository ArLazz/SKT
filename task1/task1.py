import sys

s = max(len(sys.argv[1]), len(sys.argv[2]))
args1 = list(map(float, sys.argv[1].split(',')))
args2 = list(map(float, sys.argv[2].split(',')))

for i in range(len(args1) - 2):
    if args1[i] != 0:
        print("{0}s^{1} + ".format(args1[i] if args1[i] != 1 else '', len(args1) - i - 1), end='')
print("{0}s + {1}".format(args1[-2], args1[-1]))

print('-' * s * 4)

for i in range(len(args2) - 2):
    if args2[i] != 0:
        print("{0}s^{1} + ".format(args2[i] if args2[i] != 1 else '', len(args2) - i - 1), end='')
print("{0}s + {1}".format(args2[-2], args2[-1]))
