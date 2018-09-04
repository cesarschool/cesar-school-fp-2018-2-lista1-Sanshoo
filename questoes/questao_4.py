## QUESTÃO 4 ##
# Escreva um programa que pergunte a quantidade de km percorridos por um carro 
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 
# R$ 0,15 por km rodado.

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("esse programa calcula o valor a ser pago do aluguel de um carro.")
    dias = int(input("digite a quantidade de dias que o carro passou alugado "))
    kilometros = int(input("digite a quantidade de km percorridos pelo carro enquanto alugado "))
    price = (dias*60)+(kilometros*0.15)                 
    print ("o valor total a ser pago pelo aluguel é: R$" + str(price))

    
if __name__ == '__main__':
    main()
