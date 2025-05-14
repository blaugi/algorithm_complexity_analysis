def counting_sort_digit(S, exp):
    n = len(S)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = abs(S[i]) // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = abs(S[i]) // exp
        output[count[index % 10] - 1] = S[i]
        count[index % 10] -= 1

    for i in range(n):
        S[i] = output[i]

def Radix_Sort(S):
    if not S:
        return S

    negativos = [-x for x in S if x < 0]
    positivos = [x for x in S if x >= 0]


    if positivos:
        max_val = max(positivos)
        exp = 1
        while max_val // exp > 0:
            counting_sort_digit(positivos, exp)
            exp *= 10

    if negativos:
        max_val = max(negativos)
        exp = 1
        while max_val // exp > 0:
            counting_sort_digit(negativos, exp)
            exp *= 10
        negativos = [-x for x in reversed(negativos)]

    return negativos + positivos

def Radix_Sort_interativo_wapper(A):
    return Radix_Sort(A)

# Exemplo de uso
# X = [58, 30, 97, 21, 81, 35, 48, 59, 24, 2, -1]
# print("ANTES", X)
# QQ = Radix_Sort_interativo_wapper(X)
# print("DEPOIS", QQ)