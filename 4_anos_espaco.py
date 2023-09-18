#Calcula a quantidade de anos espaciais
def f_anos_espaco(anos_terra):
    return anos_terra // 2


def main():
    #Lê a quantidade de anos terrestres
    anos_terra = int(input("Digite os anos terrestres: "))

    #Mostra o resultado da função "f_anos_espaco"
    print(f'{anos_terra} anos terrestres equivalem a {f_anos_espaco(anos_terra)} anos espaciais.')

if __name__ == '__main__':
    main()
