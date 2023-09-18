#Função para arredondar ao número
#mais próximo
def f_arredondar(dinheiro):
    return round(dinheiro)


def main():
    #Digita a quantidade a ser arredondada
    dinheiro = float(input("Insira um valor: "))

    #Exibe o resultado da função "f_arredondar"
    print(f'O valor arredondado é {f_arredondar(dinheiro)}.')

if __name__ == '__main__':
    main()
