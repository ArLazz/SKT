import sys
import numpy as np
from typing import List
import matplotlib.pyplot as plt


def input_matrix(s: str) -> List[List[float]]:
    f = open(s)
    matr = []
    try:
        for line in f:
            matr.append(list(map(float, line.split(' '))))
    except ValueError:
        print('Ошибка.')
        exit()
    except Exception:
        print('Ошибка.')
        exit()
    else:
        return matr
    finally:
        f.close()


# def transfunc(s: int) -> int:
#     i = np.diag([s] * len(a))
#     res = np.dot(np.dot(c, np.linalg.inv(i - a)), b) + d
#     return res[0][0]


a = np.array(input_matrix('A.txt'))
b = np.array(input_matrix('b.txt'))
c = np.array(input_matrix('c.txt'))
d = np.array(input_matrix('d.txt'))

if not len(a) == len(b) == len(c[0]):
    print('Ошибка.')
    exit()

fig, ax = plt.subplots()
x = np.linspace(-10, 10, 500)
y = np.array([])
for i in x:
    y = np.append(y, np.dot(np.dot(c, np.linalg.inv(np.diag([i] * len(a)) - a)), b) + d)
ax.plot(x, y)
plt.show()