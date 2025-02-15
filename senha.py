#montar programa com um loop que fique 
#pedindo para digitar senha correta ate que 
#a pessoa digitar senha 

senha = "abcd1234"
senhaDigitada ="";

while senhaDigitada != senha:
    senhaDigitada = input("Digite a senha:")
    if senhaDigitada != senha: 
        print("senha invalida")

print ("senha correta")