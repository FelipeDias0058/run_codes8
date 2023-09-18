#Função soma o preço total dos produtos comprados
def preco_total(maca, banana):
    return (3 * maca) + (2 * banana)


def main():

    #Digita o preço individual das maçãs e bananas
    maca = float(input("Valor de uma maçã: "))
    banana = float(input("Valor de uma banana: "))

    #Imprime na tela a função "preco_total",
    #formatada com f_string para exibir as
    #duas casas decimais
    print(f'O preço total da compra é R${preco_total(maca, banana):.2f}.')

if __name__ == '__main__':
    main()

    
