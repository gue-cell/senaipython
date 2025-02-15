limite = 101
contador = 0
sair = False  # true ou false 

while sair == False:
    print('contando.:', contador)
    contador  +=  1 
    resposta = input('desejar parar o contador? S/N:') 


    if resposta == 'N' :
        sair = False
    else:
        sair = True

