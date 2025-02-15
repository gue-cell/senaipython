# definir a variavel da tabuada 
# definir uma variavel de contador - variar de 1 a 10
# criar um loop
#multiplicar as variaveis e guarda  o resultado 
#mostrar o resultado
#somar 1 ao valor contador 

tabuada = 2 
contador = 1 
resultado = 0

while tabuada <= 10:
    resultado = tabuada * contador
    print(tabuada, "x",contador,"=",resultado)
    contador +=1
    if contador ==11:
        tabuada+=1
        contador=1

