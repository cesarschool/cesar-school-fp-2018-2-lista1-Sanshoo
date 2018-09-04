## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print ("esse programa calcula o aumento de um salário.")
    x = float(input("digite o salário atual "))
    y = float(input("digite o valor percentual do aumento "))
    aumento = x*(y/100)
    salario_novo = x+aumento
    print ("o valor do aumento foi de " + str(aumento) + " e o valor do salário novo salário é " + str(salario_novo))


if __name__ == '__main__':
    main()
