import numpy as np

# xb=BT*xa
# 1) Sprawdzic czy B ma wektory ortogonalne
# 2) Znormalizować wektor w B
# 3) Sprawdzić czy znormalizowana B jest ortonormalna BT*B
# 4) Przeprowadzić wektor [8, 6, 2, 3, 4, 6, 6, 5] z bazy standardowej do bazy B po normalizacji

B = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, -1, -1, -1, -1],
    [1, 1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, -1, -1],
    [1, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, -1]
], dtype=np.float_)


def zad1(B):
    B = np.dot(B, np.transpose(B))
    for i in range(len(B)):
        for j in range(len(B[i])):
            if i != j and B[i][j] != 0:
                return False
    return True


def zad2(B):
    for i in range(len(B)):
        s = 0
        for j in range(len(B[i])):
            s += B[i][j] ** 2
        n = np.sqrt(s)
        for j in range(len(B[i])):
            B[i][j] /= n
    return B


print(np.dot(B, np.transpose(B)))
print(zad1(B))
C = zad2(B)
print(C)
D = np.dot(np.transpose(C), C).astype(dtype=np.float16)
print(D)
xa = np.array([8, 6, 2, 3, 4, 6, 6, 5])
print(np.dot(np.transpose(C), xa))
