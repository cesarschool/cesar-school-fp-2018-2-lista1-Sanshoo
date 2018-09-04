## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius) 
# para °F (graus fahrenheit). 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print ("esse programa converte uma temperatura de celsius para fahrenheit.")
    temp_celsius = float(input("digite uma temperatura em graus celsius "))
    temp_fahrenheit = (1.8*temp_celsius)+32
    print ("a temperatura equivalente em fahrenheit é " + str(temp_fahrenheit))

if __name__ == '__main__':
    main()
