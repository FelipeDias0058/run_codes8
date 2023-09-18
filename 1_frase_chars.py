#Função que lê quantos caracteres tem o texto digitado
def f_texto(txt):
    return len(txt)
    
def main():
    #Entrada de Dados
    txt = input("Digite uma frase: ")
    txt = txt.strip()

    #Mostra a quantidade de caracteres na frase digitada
    print(f'A frase tem {f_texto(txt)} caracteres.')

if __name__ == '__main__':
    main()
