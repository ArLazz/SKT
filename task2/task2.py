import sys
import numpy as np
from typing import List


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


a = np.array(input_matrix('A.txt'))
b = np.array(input_matrix('b.txt'))
c = np.array(input_matrix('c.txt'))
d = np.array(input_matrix('d.txt'))
m = np.array(input_matrix('M.txt'))

if not len(a) == len(b) == len(m) == len(c[0]) and len(m) != 0:
    print('Ошибка.')
    exit()

m_inv = np.linalg.inv(m)
new_a = np.dot(np.dot(m, a), m_inv)
new_b = np.dot(m, b)
new_c = np.dot(c, m_inv)

if len(sys.argv) > 1:
    output_arg = sys.argv[1]
else:
    output_arg = ''
np.savetxt('A' + output_arg + '.txt', new_a, delimiter=' ', fmt='%1.4f')
np.savetxt('b' + output_arg + '.txt', new_b, delimiter=' ', fmt='%1.4f')
np.savetxt('c' + output_arg + '.txt', new_c, delimiter=' ', fmt='%1.4f')
np.savetxt('d' + output_arg + '.txt', d, delimiter=' ', fmt='%1.4f')
print('Программа выполнена успешно.')
