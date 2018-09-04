## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    import math
    print("esse programa calcula a área, o diâmetro e o comprimento de uma circunferência a partir de seu raio.")
    raio = float(input("digite o raio da circunferência desejada "))
    area =  math.pi*(raio**2)
    comprimento = math.pi*2*raio
    diametro = raio*2
    print("a área desse círculo é " + str(area) + ", o diâmetro é " + str(diametro) + " e o comprimento da circunferência é " + str(comprimento) + ". Tenha um ótimo dia ^^")  

    
if __name__ == '__main__':
    main()
