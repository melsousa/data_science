#IMPRIMIR UMA LISTA
def amplitude(lista):
    print(lista)

# imprimir string
def string(palavra):
    for i in range(len(palavra)):
        print(palavra[i])

# 
def peso(peso):
    if peso <= 10:
        print("O valor será R$ 50,00")
    elif peso >= 11 and peso <= 20:
        print("O valor será R$ 80,00")
    else :
        print("O transporte não é aceito")
        
def main():
    lista = [1, 2, 43, 546, 64, 2]
    amplitude(lista)
    
    palavra = 'python'
    string(palavra)
    
    pesoDaCarga = 401
    peso(pesoDaCarga)

main()