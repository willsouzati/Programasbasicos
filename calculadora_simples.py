print('SELECIONE O OPERADOR ABAIXO')
print('1 - SOMA')
print('2 - SUBTRAÇÃO')
print('3 - MULTIPLICAÇÃO')
print('4 - DIVISÃO')

opcao = input('Digite uma opção :')

if opcao == '1':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    resultado = num1 + num2
    print(f'O resultado é : {resultado}')
elif opcao == '2':
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número: '))
    resultado = num1 - num2
    print(f'O resultado é : {resultado}')

elif opcao == '3':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    resultado = num1 * num2
    print(f'O resultado é : {resultado}')
elif opcao == '4':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    if num2 != 0:
        resultado = num1 / num2 

        print(f'O resultado é: {resultado}')
    else:
        print('Impossível dividir por 0!') 
else:
    print('Opção Inválida, Tente novamente !')







