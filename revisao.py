# entrada 
numero1 = float(input(' digite um número : '))
                
numero2 = float(input ('digite outro numero :'))
print('qual operacao você deseja ? digite')
print('A - AdiÇâo')
print('S - SubtraÇâo')
print('M - Multiplicaçâo')
print('D- Divisão ')
print('E- Exponenciaçâo')
operacao = input (' qual sua escolha ?')

# processamento
resultado = 0 
if (operacao .upper () == 'A') :
    resultado = numero1 + numero2
elif (operacao .upper () == 'S') :
    resultado = numero1 - numero2
elif (operacao .upper () == 'M') :
    resultado = numero1 * numero2
elif (operacao .upper () == 'D') :
    resultado = numero1 / numero2
elif(operacao .upper () == 'E') :
    resultado = numero1 ** numero2
else:print ('opção invàlida.')


# saida 
print ( 'o resultado é :' , resultado)
