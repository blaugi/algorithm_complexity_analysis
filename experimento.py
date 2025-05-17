import sys
import pandas as pd

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

    # print("Starting QS1 sort...")
    # a = agora()
    # QS1 = quick_sort_recursivo_wapper(X.copy())
    # b = agora()
    # elapsed = dif_time(b, a)
    # D.append(elapsed)
    # print(f"Finished QS1 sort in {elapsed}")

    print("Starting QS2 sort...")
    a = agora()
    QS2 = quick_sort_recursivo_random_wapper(X.copy())
    b = agora()
    elapsed = dif_time(b, a)
    D.append(elapsed)
    print(f"Finished QS2 sort in {elapsed}")

    # print("Starting MS1 sort...")
    # a = agora()
    # MS1 = Merge_Sort_interativo_wapper(X.copy())
    # b = agora()
    # elapsed = dif_time(b, a)
    # D.append(elapsed)
    # print(f"Finished MS1 sort in {elapsed}")

    # print("Starting MS2 sort...")
    # a = agora()
    # MS2 = merge_sort__recursivo_wapper(X.copy())
    # b = agora()
    # elapsed = dif_time(b, a)
    # D.append(elapsed)
    # print(f"Finished MS2 sort in {elapsed}")

    # print("Starting MS3 sort...")
    # a = agora()
    # MS3 = merge_sort_recursivo_random_wapper(X.copy())
    # b = agora()
    # elapsed = dif_time(b, a)
    # D.append(elapsed)
    # print(f"Finished MS3 sort in {elapsed}")

    # print("Starting SS1 sort...")
    # a = agora()
    # SS1 = select_sort_recursivo_wapper(X.copy())
    # b = agora()
    # elapsed = dif_time(b, a)
    # D.append(elapsed)
    # print(f"Finished SS1 sort in {elapsed}")

    # print("Starting SS2 sort...")
    # a = agora()
    # SS2 = select_sort_recursivo_random_wapper(X.copy())
    # b = agora()
    # elapsed = dif_time(b, a)
    # D.append(elapsed)
    # print(f"Finished SS2 sort in {elapsed}")

    # print("Starting INT sort...")
    # a = agora()
    # INT = intro_sort_interativo_wapper(X.copy())
    # b = agora()
    # elapsed = dif_time(b, a)
    # D.append(elapsed)
    # print(f"Finished INT sort in {elapsed}")

    # print("Starting RAD sort...")
    # a = agora()
    # RAD = Radix_Sort_interativo_wapper(X.copy())
    # b = agora()
    # elapsed = dif_time(b, a)
    # D.append(elapsed)
    # print(f"Finished RAD sort in {elapsed}")

    # print("Starting BASE_LINE sort...")
    # a = agora()
    # BASE_LINE = shellSort_Wapper(X.copy())
    # b = agora()
    # elapsed = dif_time(b, a)
    # D.append(elapsed)
    # print(f"Finished BASE_LINE sort in {elapsed}")

    return D

limite = sys.getrecursionlimit()
print('Limite de memória: ', limite)
sys.setrecursionlimit(100000)
limite = sys.getrecursionlimit()
print('Limite de memória: ', limite)

T = 1000000
N = 10
L = [["QS1","QS2","MS1","MS2","MS3","SS1","SS2","INT","RAD","BASE_LINE"]]


for i in range(1, N+1, 1):
    print('O tamanho do problema',i, ' é ', i * T)
    X = gerar_dados_random( i * T )
    L.append( execucao(X, i) )

df_random = pd.DataFrame(L)

L = [["QS1","QS2","MS1","MS2","MS3","SS1","SS2","INT","RAD","BASE_LINE"]]
for i in range(1, N+1, 1):
    print('O tamanho do problema',i, ' é ', i * T)
    X = gerar_dados_decrescente( i * T )
    L.append( execucao(X, i) )

df_descrescente = pd.DataFrame(L)

L = [["QS1","QS2","MS1","MS2","MS3","SS1","SS2","INT","RAD","BASE_LINE"]]
for i in range(1, N+1, 1):
    print('O tamanho do problema',i, ' é ', i * T)
    X = gerar_dados_crescente( i * T )
    L.append( execucao(X, i) )

df_crescente = pd.DataFrame(L)

writer = pd.ExcelWriter('dados.xlsx', engine='xlsxwriter')
df_random.to_excel(writer, sheet_name='Sheet1')
df_descrescente.to_excel(writer, sheet_name='Sheet2')
df_crescente.to_excel(writer, sheet_name='Sheet3')

writer.close()