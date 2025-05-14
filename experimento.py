import sys

from quick_sort_recursivo import quick_sort_recursivo_wapper
from quick_sort_random import quick_sort_recursivo_random_wapper
from merge_sort_interativo import Merge_Sort_interativo_wapper
from merge_sort_recursivo import merge_sort__recursivo_wapper
from merge_sort_recursivo_random import merge_sort_recursivo_random_wapper
from select_sort_recursivo import select_sort_recursivo_wapper
from select_sort_recursivo_random import select_sort_recursivo_random_wapper
from sellSort_base_line import shellSort_Wapper
from intro_sort import intro_sort_interativo_wapper
from radix_sort import Radix_Sort_interativo_wapper
from gerador import gerar_dados_crescente
from gerador import gerar_dados_random
from gerador import gerar_dados_decrescente
from gerador import agora
from gerador import dif_time


def execucao(X, i):
    D = []

    a = agora()
    QS1 = quick_sort_recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    QS2 = quick_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    MS1 = Merge_Sort_interativo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    MS2 = merge_sort__recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    MS3 = merge_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    SS1 = select_sort_recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    SS2 = select_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    INT = intro_sort_interativo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    RAD = Radix_Sort_interativo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    a = agora()
    BASE_LINE = shellSort_Wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    return D

limite = sys.getrecursionlimit()
print('Limite de memória: ', limite)
sys.setrecursionlimit(100000)
limite = sys.getrecursionlimit()
print('Limite de memória: ', limite)

T = 1000
N = 10
L = []

for i in range(1, N+1, 1):
    print('O tamanho do problema',i, ' é ', i * T)
    X = gerar_dados_random( i * T )
    L.append( execucao(X, i) )

print('QS1,QS2,MS1,MS2,MS3,SS1,SS2,BASE_LINE,INTRO,RADIX')
for x in L:
    c = len(x) - 1
    i = 0
    for y in x:
        if (i < c):
            print(y, end=',')
        else:
            print(y, end='')
        i +=1
    print()

