import sys
import numpy as np
import cmath
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

# omega = np.linspace(0, 5, 100)
# # w = np.dot(np.dot(c, np.linalg.inv(np.diag([1j*omega] * len(a)) - a)), b) + d
# plt.figure(1)
# plt.scatter(w.real, w.imag)
# plt.show()

omega = np.linspace(0.01, 10, 1000)
T = 1
j = complex(0, 1)
# Aw = 20 * cmath.log10(abs(1 / ((omega * j * T) ** 2 + omega * j + 1)))
# phi = cmath.phase((1 / ((omega * j * T) ** 2 + omega * j + 1)))
Aw = np.array([])
phi = np.array([])
for i in omega:
    Aw = np.append(Aw, 20 * cmath.log10(abs(np.dot(np.dot(c, np.linalg.inv(np.diag([i * j * T] * len(a)) - a)), b) + d)))
    phi = np.append(phi, cmath.phase(np.dot(np.dot(c, np.linalg.inv(np.diag([i * j * T] * len(a)) - a)), b) + d))
    # Aw = np.append(Aw, 20 * cmath.log10(abs(1 / ((i * j * T) ** 2 + i * j + 1))))//для примера
    # phi = np.append(phi, cmath.phase((1 / ((i * j * T) ** 2 + i * j + 1))))//для примера

fig, ax = plt.subplots(2)
fig.suptitle('Диаграмма Боде')
ax[0].plot(omega, Aw)
ax[0].set_title('ЛАЧХ')
ax[0].set_xscale('log')
ax[1].plot(omega, phi)
ax[1].set_title('ЛФЧХ')
ax[1].set_xscale('log')

plt.show()
