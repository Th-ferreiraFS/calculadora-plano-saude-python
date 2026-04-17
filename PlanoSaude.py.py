#Criação de um algoritmo de plano de saude
print(" " + "_" * 44)
print("|  Bem vindos ao programa de Thiago Ferreira!|")
print("|"+"_" * 44 +"|")
print(" " *44)

#captura dovalor do plano
valorplano = float(input("Qual valor do plano ?"))
#caputuração da idade
idade = int(input("Digite sua idade para saber o valor do plano: "))

if idade <19: #se idade for menor que 19
         valorplano = valorplano *1.0 #calcular 100%
elif idade < 29: #se idade for menor que 29 e maior que 19
    valorplano = valorplano *1.5 #calcular 150%
elif idade < 39: #se idade for menor que 39 e maior que 29
        valorplano = valorplano *2.25 #calcular 225%
elif idade < 49: #se idade for menor que 49 e maior que 39
          valorplano = valorplano *2.4 #calcular 240%
elif idade < 59: #se idade for menor que 59 e maior que 49
           valorplano = valorplano *3.5 #calcular 350%
else: 
    valorplano = valorplano *6.0 # se idade for maior que 59, calcula 600%

print("O valor sera", valorplano ) 

