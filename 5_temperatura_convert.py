#Converte Fahrenheit para Celsius
def f_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32

def main():
    #Entrada de Dados
    celsius = float(input("Digite a temperatura em Celsius: "))

    #Mostra a quantidade de graus em Fahrenheit
    print(f'A temperatura em Fahrenheit é de {f_fahrenheit(celsius):.2f} graus.')

if __name__ == '__main__':
    main()
