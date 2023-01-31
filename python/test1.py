from statistics import mean, median
from numpy import *

z = [1, 2, 3, 4, 5]
a = random.random((8,8))

print(mean(z))
print(median(z))

#dicionários, conjuntos com chave
notas = {'joao': 6, 'maria': 8, 'pedro':9}

print(notas['maria'])
print('chaves:', notas.keys(), 'valores:',notas.values())

#set , conjuntos não ordenados de elementos não repetidos
bigdata = {'spark', 'hive', 'sqoop'}
print(bigdata)

#add elemento
bigdata.add('hadoop')
print(bigdata)

#numero de elementos
print(len(bigdata))

#tupla, listas que não podem ser alteraddas
tupla = (1,2,3,4,5,6,7)
print(tupla)