 # Recebe a entrada do usuário
letra = input('Digite uma letra do alfabeto: ')
 # Converte a letra em minúscula para evitar problemas 
letra = letra.lower()
 # Verifica a letra digitada e mostra o objeto correspondente
if letra == 'a':
    print('Avião')
elif letra == 'b':
    print('Bola')
elif letra == 'c':
    print('Carro')
elif letra == 'd':
    print('Dado')
elif letra == 'e':
    print('Elefante')
elif letra == 'f':
    print('Foca')
elif letra == 'g':
    print('Gato')
elif letra == 'h':
    print('Hipopótamo')
elif letra == 'i':
    print('Igreja')
elif letra == 'J':
    print('Janela')
elif letra == 'u':
    print('Uva')
elif letra == 'k':
    print('Kalunga')
 # fazer o mesmo com as outras letras do alfabeto até...
else:
    print('Não conheço uma palavra que comece com essa letra.')